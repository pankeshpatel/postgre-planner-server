from fastapi import APIRouter, status, Response, HTTPException, Depends, BackgroundTasks
#from schemas.user import User
from datetime import datetime, date
import platform
import os
import sys
import math
import datetime  # one of the functions doesnt work unless I have this line, idk
from datetime import date
import pandas as pd
from typing import List, Tuple, Set, Dict
from typing import Optional
import json
from tabulate import tabulate

from config.oauth2 import get_current_user



#Redis
from config.redisdb import redis_db
my_redis = redis_db()

from sqlalchemy.orm import Session
from config.db import get_db

import asyncio


# Create a new instance of simple profiler
from config.profiler import profiler
my_profiler = profiler()


# postgre
from config.db import get_db
from sqlalchemy.orm import Session
from models.dbschema import *


healthscore = APIRouter(
    prefix = "/healthscore",
    tags=["health score"],
)

saftey_stock : int
stock: int
avg_stock_change: float



# This function constructs an individual instances of total Quantity fields
def find_total_quantity_instances(formatted_date: str, material_id: str, 
                                  safety_stock: int, data:pd.DataFrame(), list_qty_instance: List):
        
    item=0
    local_list_qty_instance = []
    #global list_qty_instance
    
    
    if(len(data) == 0):
        local_list_qty_instance = [
            material_id,
            formatted_date,
            0,
            safety_stock
        ]
        list_qty_instance.append(local_list_qty_instance)        
        
    else:
        while(item < len(data)):
            local_list_qty_instance = [
                data["material"][item],
                data["demand_date"][item],
                data["total_quantity"][item],
                safety_stock
            ]
            
            list_qty_instance.append(local_list_qty_instance)        
            item = item + 1
            
    return list_qty_instance


# This function  constructs a summary (avg, min, max) dataframe total Quantity
def find_total_quantity_summary(formatted_date: str, material_id: str, 
                                safety_stock: int, data:pd.DataFrame(), list_qty: List):

    # max value
    if(len(data["total_quantity"]) == 0):
        max, min, mean = 0,0,0
    else:
        max = data["total_quantity"].max()
        min = data["total_quantity"].min()
        mean = data["total_quantity"].mean()

    
    local_list_qty = []    
    local_list_qty = [
        material_id, 
        formatted_date, 
        max, 
        min, 
        round(mean,2), 
        safety_stock
        ]
            
    # construct a list
    list_qty.append(local_list_qty)    
    
    return list_qty



# This function is to find stock
def find_stock(date: str, formatted_date: str, material_id: str, data:pd.DataFrame()) -> int:
            
    # Data is not available in DB
    if(len(data) == 0):
        print("No data found for", formatted_date)
        return 0
        #return None 
    
    if "Stock" in data.values:
        data_stock = data[data["mrp_element"] == "Stock"]
        for index, row in data_stock.iterrows(): 
            if date == row[2]:
                return row["total_quantity"]
    else:
        # # If else no concrete "Stock" data present just take stock for first entry of that day
        data_date = data[data["demand_date"] == formatted_date]
        for index, row in data_date.iterrows():
            # Assuming data sorted, returning first total_quantity entry for that data
            return row["total_quantity"]


def find_saftey_stock(data: pd.DataFrame(), saftey_stock: int) -> int:
    
    for index, row in data.iterrows():   
        safety_stock_qty = abs(row["change_quantity"])    
        return abs(row["change_quantity"])  

    # Else
    safety_stock_qty = abs(saftey_stock) 

    return abs(saftey_stock)  


def format_date(date: datetime) -> str:
    return datetime.date.strftime(date, "%x")



# What is sigmoid function - https://www.youtube.com/watch?v=LcHYy-OZHp8
def get_health_score(stock: int, saftey_stock: int, k_val: float) -> float:
    
    if stock != None and saftey_stock != 0:
        return sigmoid(SS=(stock/saftey_stock), k=k_val)
    else:
        return 0.00



def sigmoid(SS: int, k: float) -> float:
    return (((1/(1+math.exp(-k*SS)))-(1/2))*2)*100



@healthscore.get('/{planner_id}/{material_id}', status_code = status.HTTP_200_OK)
async def get_material_healthscore(planner_id:str, material_id: str, healthdate: str, db : Session = Depends(get_db), current_user : int = Depends(get_current_user)):

    material_healthscore_key = "healthscore" + "/" + planner_id + "/" + material_id + "/" + healthdate
    redis_reponse = my_redis.get(material_healthscore_key)
    

     # Check if the data exists in Cache
    if redis_reponse != None:
        print("Found the results in redis cache.......healthscore()")
        
        # update the cache 1 days advance 
        date = healthdate       
        mm, dd, yyyy = map(int, date.split('/'))
        date_obj = datetime.datetime(yyyy, mm, dd)
        td = datetime.timedelta(days=1)
        new_date = date_obj + td

        formatted_date = format_date(date=new_date)
        asyncio.create_task(get_material_healthscore_background(planner_id, material_id, formatted_date, db))
        return json.loads(redis_reponse)
    else:
        print("I have not found the results in redis cache, computing now...")   
        my_profiler.start("health-score")
        date = healthdate
        num_days = 10  
        
        
        #sql = """SELECT mrp_element, change_quantity FROM admin.MD04 where material = %s AND planner=%s"""
        #data_safety_stock = pd.DataFrame(conn.execute(sql, material_id, planner_id).fetchall())

        data = db.query(MD04.mrp_element, MD04.change_quantity).where(MD04.material == material_id).where(MD04.planner == planner_id).all()
        data_safety_stock = pd.DataFrame(data, columns=["mrp_element", "change_quantity"])


        if len(data_safety_stock.columns) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Data item does not exist")


        saftey_stock = 0 # default value 
        saftey_stock = find_saftey_stock(data_safety_stock[data_safety_stock["mrp_element"] == "SafeSt"], saftey_stock)


        mm, dd, yyyy = map(int, date.split('/'))
        date_obj = datetime.datetime(yyyy, mm, dd)
        avg: List = []  # List to keep track of health scores
        list_qty: List = []
        list_qty_instance : List = []
        
        # This loop will get 
        for i in range(int(num_days)):
            td = datetime.timedelta(days=i)
            new_date = date_obj + td
            
            formatted_date = format_date(date=new_date)
            
            # sql = """SELECT material, mrp_element, total_quantity, demand_date  FROM admin.MD04 WHERE material = %s AND demand_date = %s"""
            # data= pd.DataFrame(conn.execute(sql, material_id, formatted_date).fetchall(), columns=["material", "mrp_element", "total_quantity", "demand_date" ])
            
            data_q = db.query(MD04.material, MD04.mrp_element, MD04.total_quantity, MD04.demand_date).where(MD04.material == material_id).where(MD04.demand_date == formatted_date).all()
            data = pd.DataFrame(data_q, columns=["material", "mrp_element", "total_quantity", "demand_date" ])
            
            stock = find_stock(new_date, formatted_date, material_id, data)
            
            
            list_qty = find_total_quantity_summary(formatted_date, material_id, saftey_stock, data, list_qty)             
            
            list_qty_instance= find_total_quantity_instances(formatted_date, material_id, saftey_stock, data, list_qty_instance) 
             
            health = get_health_score(stock, saftey_stock, k_val=0.8)   
            
            if health != None:
                avg.append(health)


        df_total_qty = pd.DataFrame(list_qty, columns = ['material', 'demand_date', 'max', 'min', 'mean', 'safety stock']) 
        print(tabulate(df_total_qty, headers = 'keys', tablefmt = 'psql'))
        
        
        # This would prepare .csv file that contains total_qty_instances
        df_total_qty_instances = pd.DataFrame(list_qty_instance, columns = ['material', 'demand_date', 'total_quantity', 'safety stock'])
        
        print(tabulate(df_total_qty_instances, headers = 'keys', tablefmt = 'psql'))
        
        
        result = sum(avg)/len(avg)
        result = round(result, 2)
        percentage_result = str(result).__add__(' %')
        
        data = db.query(MaterialMaster.material, MaterialMaster.mat_description_eng).where(MaterialMaster.material == material_id)
        df_material = pd.DataFrame(data, columns=["material", "mat_description_eng"])


        health_score = {
            "Material": material_id,
            "material_detail" : json.loads(json.dumps(list(df_material.T.to_dict().values()))),
            "Date": date,
            "Health-score": percentage_result,
            "total_qty_analysis" : json.loads(json.dumps(list(df_total_qty.T.to_dict().values()))),
            "total_qty_instances": json.loads(json.dumps(list(df_total_qty_instances.T.to_dict().values())))    
        }
        
        my_profiler.end("health-score")
        my_profiler.log("print")

        # 172800 seconds = 2 days
        my_redis.put(material_healthscore_key, json.dumps(health_score), 172800)
                

        return health_score


async def get_material_healthscore_background(planner_id:str,  material_id: str, healthdate: str, db):

    material_healthscore_key = "healthscore" + "/" + planner_id + "/" + material_id + "/" + healthdate
    redis_reponse = my_redis.get(material_healthscore_key)
    
     # Check if the data exists in Cache
    if redis_reponse != None:
        print("Found the results in redis cache.......")
        
    else:
        print("I have not found the results in redis cache, computing now...")   
        date = healthdate
        num_days = 10  
        
        
        # sql = """SELECT mrp_element, change_quantity FROM admin.MD04 where material = %s AND planner=%s"""
        # data_safety_stock = pd.DataFrame(conn.execute(sql, material_id, planner_id).fetchall())
        
        data = db.query(MD04.mrp_element, MD04.change_quantity).where(MD04.material == material_id).where(MD04.planner == planner_id).all()
        data_safety_stock = pd.DataFrame(data, columns=["mrp_element", "change_quantity"])
        
        
        if len(data_safety_stock.columns) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Data item does not exist")


        saftey_stock = 0 # default value 
        saftey_stock = find_saftey_stock(data_safety_stock[data_safety_stock["mrp_element"] == "SafeSt"], saftey_stock)


        mm, dd, yyyy = map(int, date.split('/'))
        date_obj = datetime.datetime(yyyy, mm, dd)
        avg: List = []  # List to keep track of health scores
        list_qty: List = []
        list_qty_instance : List = []
        
        
        
        # This loop will get 
        for i in range(int(num_days)):
            td = datetime.timedelta(days=i)
            new_date = date_obj + td
            
            formatted_date = format_date(date=new_date)
            
            # sql = """SELECT material, mrp_element, total_quantity, demand_date  FROM admin.MD04 WHERE material = %s AND demand_date = %s"""
            # data= pd.DataFrame(conn.execute(sql, material_id, formatted_date).fetchall(), columns=["material", "mrp_element", "total_quantity", "demand_date" ])
            
            data_q = db.query(MD04.material, MD04.mrp_element, MD04.total_quantity, MD04.demand_date).where(MD04.material == material_id).where(MD04.demand_date == formatted_date).all()
            data = pd.DataFrame(data_q, columns=["material", "mrp_element", "total_quantity", "demand_date" ])
                        
            stock = find_stock(new_date, formatted_date, material_id, data)
            list_qty = find_total_quantity_summary(formatted_date, material_id, saftey_stock, data, list_qty) 
            list_qty_instance = find_total_quantity_instances(formatted_date, material_id, saftey_stock, data, list_qty_instance)  
            health = get_health_score(stock, saftey_stock, k_val=0.8)   
            
            if health != None:
                avg.append(health)


        df_total_qty = pd.DataFrame(list_qty, columns = ['material', 'demand_date', 'max', 'min', 'mean', 'safety stock']) 
        print(tabulate(df_total_qty, headers = 'keys', tablefmt = 'psql'))
        
        
        # This would prepare .csv file that contains total_qty_instances
        df_total_qty_instances = pd.DataFrame(list_qty_instance, columns = ['material', 'demand_date', 'total_quantity', 'safety stock'])
        print(tabulate(df_total_qty_instances, headers = 'keys', tablefmt = 'psql'))
        
        
        result = sum(avg)/len(avg)
        result = round(result, 2)
        percentage_result = str(result).__add__(' %')
        
        #sql = """SELECT DISTINCT material, material_9, material_7, mat_description, mat_description_eng FROM admin.MaterialMaster where material = %s"""
        #df_material = pd.DataFrame(conn.execute(sql, material_id).fetchall(), columns=["material", "material_9" , "material_7", "mat_description", "mat_description_eng"])
        
        data = db.query(MaterialMaster.material,  MaterialMaster.material_9,  MaterialMaster.material_7,  MaterialMaster.mat_description,  MaterialMaster.mat_description_eng).where(MaterialMaster.material == material_id)
        df_material = pd.DataFrame(data,  columns=["material", "material_9" , "material_7", "mat_description", "mat_description_eng"])
        


        health_score = {
            "Material": material_id,
            "material_detail" : json.loads(json.dumps(list(df_material.T.to_dict().values()))),
            "Date": date,
            "Health-score": percentage_result,
            "total_qty_analysis" : json.loads(json.dumps(list(df_total_qty.T.to_dict().values()))),
            "total_qty_instances": json.loads(json.dumps(list(df_total_qty_instances.T.to_dict().values())))    
        }
        

        # 172800 seconds = 2 days
        my_redis.put(material_healthscore_key, json.dumps(health_score), 172800)

from fastapi import APIRouter, status, HTTPException, Depends
from config.db import conn
from schemas.user import User
from datetime import datetime, date
from models.dbschema import dbMaterialMaster
import pandas as pd
import json
from config.oauth2 import get_current_user

from config.redisdb import redis_db
my_redis = redis_db()

from sqlalchemy.orm import Session
from config.db import get_db


material = APIRouter(
    prefix = "/materials",
    tags=["materials"]
)



# async def get_all_material_info(planner_id: str, user_id: int = Depends(get_current_user), session: Session = Depends(get_db)):
@material.get('/{planner_id}',status_code = status.HTTP_200_OK)
async def get_all_material_info(planner_id: str):
    
    # Redis caching
    material_planner_id_key = "materials" + "/" + planner_id
    redis_reponse = my_redis.get(material_planner_id_key)
    
    if redis_reponse != None:
        print("Found the results in redis cache.......get_all_material_info")
        return json.loads(redis_reponse)
    else:

        sql = """SELECT DISTINCT material, material_9, material_7, mat_description, 
        mat_description_eng, safety_stock, plant, lot_size FROM admin.MaterialMaster  WHERE planner = %s"""
        
        df_material_master = pd.DataFrame(conn.execute(sql, planner_id).fetchall(), columns=["material", "material_9", "material_7", "mat_description", "mat_description_eng", "safety_stock", "plant", "lot_size"])
        
        

        df_material_master = df_material_master.drop_duplicates(subset=['material'])
                
        response = {
            "planner" : planner_id,
            "result": json.loads(json.dumps(list(df_material_master.T.to_dict().values())))     
        }
        
        my_redis.put(material_planner_id_key, json.dumps(response), 950400)
        return response



# async def get_material_info(planner_id : str, material_id:str, user_id: int = Depends(get_current_user), session: Session = Depends(get_db)):

@material.get('/{planner_id}/{material_id}', status_code = status.HTTP_200_OK)
async def get_material_info(planner_id : str, material_id:str):
    
    sql = """SELECT DISTINCT material, material_9, material_7, mat_description, mat_description_eng, safety_stock, plant, lot_size FROM admin.MaterialMaster WHERE planner = %s AND material = %s"""
    df_material_planner_master = pd.DataFrame(conn.execute(sql, planner_id, material_id).fetchall(), columns=["material", "material_9", "material_7", "mat_description", "mat_description_eng", "safety_stock", "plant", "lot_size" ])
    
    
    response = {
        "planner" : planner_id,
        "material" : material_id,
        "result": json.loads(json.dumps(list(df_material_planner_master.T.to_dict().values())))     
    }
    
    return response




from fastapi import APIRouter, status, HTTPException, Depends

import pandas as pd
import json


# Postgres 
from config.db import get_db
from models.dbschema import Planner
from sqlalchemy.orm import Session


# Redis
from config.redisdb import redis_db
my_redis = redis_db()



planner = APIRouter(
    prefix = "/planners",
    tags=["planners"]
)


    
@planner.get('/',  status_code = status.HTTP_200_OK)
async def get_all_material_planner_info(db : Session = Depends(get_db)):
    
    data = db.query(Planner.id, Planner.name, Planner.email).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items are not found")
        
    return data


    
    
@planner.get('/planner-id/{id}',  status_code = status.HTTP_200_OK)
async def get_material_planner_info(id:str, db : Session = Depends(get_db)):
    
    planner_id_key = "planners" + "/" + "planner-id" + "/" + id
    redis_reponse = my_redis.get(planner_id_key)
    
    if redis_reponse != None:
        print("Found the results in redis cache.......get_material_planner_info()")
        return redis_reponse
    
    else:
        print("I have not found the results in redis cache, computing now...get_material_planner_info()")   

        data = db.query(Planner.id, Planner.name, Planner.email).where(Planner.id == id).all()
        df_planner = pd.DataFrame(data, columns=["id", "name", "email"])
        
        if len(df_planner.columns) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Data item does not exist")
        

        my_redis.put(planner_id_key, json.dumps(list(df_planner.T.to_dict().values())), 950400)
        return json.dumps(list(df_planner.T.to_dict().values()))



@planner.get('/planner-name/{name}',  status_code = status.HTTP_200_OK)
async def get_material_planner_info(name:str, db : Session = Depends(get_db)):
        
    data = db.query(Planner.id, Planner.name, Planner.email).where(Planner.name == name).all()

    
    if not data:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items are not found")
    
    return data
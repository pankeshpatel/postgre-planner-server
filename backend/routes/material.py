from fastapi import APIRouter, status, HTTPException, Depends
#from config.db import conn
from schemas.user import User
from datetime import datetime, date
#from models.dbschema import dbMaterialMaster
import pandas as pd
import json
#from config.oauth2 import get_current_user

from config.redisdb import redis_db
my_redis = redis_db()

from sqlalchemy.orm import Session
from config.db import get_db

# postgre
from config.db import get_db
from models.dbschema import MaterialMaster
from sqlalchemy.orm import Session


material = APIRouter(
    prefix = "/materials",
    tags=["materials"]
)




@material.get('/{planner_id}',status_code = status.HTTP_200_OK)
async def get_all_material_info(planner_id: str, db : Session = Depends(get_db)):
    
    print("I am in get_all_material_info().... ")
    
    # Redis caching
    material_planner_id_key = "materials" + "/" + planner_id
    redis_reponse = my_redis.get(material_planner_id_key)
    
    if redis_reponse != None:
        print("Found the results in redis cache.......get_all_material_info")
        return json.loads(redis_reponse)
    else:
        
        data = db.query(MaterialMaster.material, 
                        MaterialMaster.material_9, 
                        MaterialMaster.material_7, 
                        MaterialMaster.mat_description, 
                        MaterialMaster.mat_description_eng, 
                        MaterialMaster.safety_stock, 
                        MaterialMaster.plant, 
                        MaterialMaster.lot_size).where(MaterialMaster.planner == planner_id).all()

        
        df_material_master = pd.DataFrame(data, columns=["material", "material_9", "material_7", "mat_description", "mat_description_eng", "safety_stock", "plant", "lot_size"])
        
        df_material_master = df_material_master.drop_duplicates(subset=['material'])
                
        response = {
            "planner" : planner_id,
            "result": json.loads(json.dumps(list(df_material_master.T.to_dict().values())))     
        }
        
        my_redis.put(material_planner_id_key, json.dumps(response), 950400)
        return response



@material.get('/{planner_id}/{material_id}', status_code = status.HTTP_200_OK)
async def get_material_info(planner_id : str, material_id:str, db : Session = Depends(get_db)):
    
    
    data = db.query(MaterialMaster.material, 
                        MaterialMaster.material_9, 
                        MaterialMaster.material_7, 
                        MaterialMaster.mat_description, 
                        MaterialMaster.mat_description_eng, 
                        MaterialMaster.safety_stock, 
                        MaterialMaster.plant, 
                        MaterialMaster.lot_size).where(MaterialMaster.planner == planner_id).where(MaterialMaster.material == material_id).all()
    
    
    df_material_planner_master = pd.DataFrame(data, columns=["material", "material_9", "material_7", "mat_description", "mat_description_eng", "safety_stock", "plant", "lot_size" ])
    
    
    df_material_planner_master = df_material_planner_master.drop_duplicates(subset=['material'])


    response = {
        "planner" : planner_id,
        "material" : material_id,
        "result": json.loads(json.dumps(list(df_material_planner_master.T.to_dict().values())))     
    }
    
    return response




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db import engine, get_db
from models.dbschema import *
from routes.index import *


#Base.metadata.create_all(bind=engine)



origins = [
   "*"
]


description = """
This is a MPA WebServer. 
It implements various APIs for the development of  MPA Dashboard and AI-based Forecasting Model 🚀

"""

app = FastAPI(title="Material Planner Assistant",
    description=description,
    version="0.0.1")


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
 )

@app.get("/")
def root():
   return {"hello" : "world"}


app.include_router(planner)
app.include_router(material)
app.include_router(healthscore)
app.include_router(exception)
app.include_router(ranking)
app.include_router(authentication)

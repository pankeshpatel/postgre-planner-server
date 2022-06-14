import psycopg2
from psycopg2.extras import RealDictCursor
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.env import settings


#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root123@localhost/postgres"

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(settings.DB_USER, settings.DB_PASSWORD, settings.DB_HOST, settings.DB_PORT , settings.DATABASE)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host = 'localhost',
#             database = 'postgres',
#             user = 'postgres',
#             password = 'root123',
#             cursor_factory = RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("Postgres database connection was succesful...")
#         break 
#     except Exception as error:
#         print(error)
#         time.sleep(5)    
    



# connect_string = f'mysql+pymysql://root:root123@localhost:3306/admin?charset=utf8mb4'


# DB_USER="root"
# DB_PASSWORD="root123"
# DB_HOST="mysql"
# DB_PORT="3306"
# DATABASE="admin"


# connect_string = 'mysql+pymysql://{}:{}@{}/{}?port={}?charset=utf8'.format(DB_USER, DB_PASSWORD, DB_HOST, DATABASE, DB_PORT)




#connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(settings.DB_USER, settings.DB_PASSWORD, settings.DB_HOST, settings.DB_PORT, settings.DATABASE)



#connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(settings.DB_USER, settings.DB_PASSWORD, settings.DB_HOST, settings.DB_PORT, settings.DATABASE)


#connect_string = f'mysql+pymysql://{}:{}@{}/{}?port={}?charset=utf8mb4'.format(DB_USER, DB_PASSWORD, DB_HOST, DATABASE, DB_PORT)
#connect_string = f'mysql+pymysql://root:admin@localhost/admin?charset=utf8mb4'
#connect_string = f'mysql+pymysql://root:admin@localhost:3306/admin?charset=utf8'

#connect_string = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}?charset=utf8'




# engine = create_engine(connect_string)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# meta = MetaData()
# conn = engine.connect()


# def get_db():
#     """
#     Function to generate db session
#     :return: Session
#     """
#     db = None
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()



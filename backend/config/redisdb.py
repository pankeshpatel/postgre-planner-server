#from redis import Redis
import json
import sys
import redis
from config.env import settings



def redis_db():
    return Cachedis()


class Cachedis(object):
    
    def __init__(self, host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0):
        
        try:
            self.__redis = redis.Redis(host, port, db)
            self.__redis.ping()
        except redis.exceptions.RedisError as error:
            print(error)
       

    def put(self, key, value, expiration_time=3600):
        self.__redis.set(key, value, expiration_time)
        
    def get(self, key):        
        return self.__redis.get(key)
        
    def remove(self, key):       
        return self.__redis.lpop(key)
        
    def clear(self):
        self.__redis.flushdb()


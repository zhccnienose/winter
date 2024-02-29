from flask_sqlalchemy import SQLAlchemy
import redis

db = SQLAlchemy()

r = redis.StrictRedis(host='', port=6379, password='')

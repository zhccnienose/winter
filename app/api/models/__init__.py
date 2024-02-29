from flask_sqlalchemy import SQLAlchemy
import redis

db = SQLAlchemy()
r = redis.StrictRedis()

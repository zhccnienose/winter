from flask_sqlalchemy import SQLAlchemy
import redis

db = SQLAlchemy()
# r = redis.StrictRedis(host='192.168.74.128', port=6379, password='310257813')
r = redis.StrictRedis(host='47.115.212.55', port=6379, password='310257813')

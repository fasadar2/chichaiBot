from peewee import *
import os
dbUsername = os.environ['POSTGRES_USER']
dbPassword = os.environ['POSTGRES_PASSWORD']
dbName = os.environ['POSTGRES_DB']
db = PostgresqlDatabase(dbName, host='postgres', port=5432, user=dbUsername, password=dbPassword)
class BaseModel(Model):
    class Meta:
        database = db  # соединение с базой, из шаблона выше


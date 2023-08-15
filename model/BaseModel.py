from peewee import *

db = PostgresqlDatabase('chichai', host='localhost', port=5432, user='postgres', password='1')
class BaseModel(Model):
    class Meta:
        database = db  # соединение с базой, из шаблона выше


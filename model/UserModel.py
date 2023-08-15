from BaseModel import *
from peewee import *
class UserModel(BaseModel):
    user_id = IntegerField(column_name="id",unique=True,primary_key=True)
    identity = CharField(column_name="identity",max_length=250)
    class Meta:
        table_name = "user"
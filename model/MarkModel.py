from BaseModel import *
from peewee import *
from UserModel import *
from BookModel import *

class MarkModel(BaseModel):
    mark_id = IntegerField(column_name="id",primary_key=True)
    user_id = ForeignKeyField(column_name="user_id",lazy_load=False,model=UserModel)
    book_id = ForeignKeyField(column_name="book_id",lazy_load=False,model=BookModel)
    date = DateTimeField(column_name="date")
    class Meta:
        table_name = "mark"
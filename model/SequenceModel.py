from BaseModel import *
from peewee import *
from BookModel import *
class SequenceModel(BaseModel):
    sequence_id = IntegerField(column_name="id",unique=True,primary_key=True)
    start_date = DateTimeField(column_name="start_date",null=False)
    end_date = DateTimeField(column_name="end_date",null = False)
    book_id = ForeignKeyField(model=BookModel,column_name="book_id",lazy_load=False)
    class Meta:
        table_name = "sequence"
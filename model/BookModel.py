from model.BaseModel import BaseModel
from peewee import *


class BookModel(BaseModel):
    book_id = IntegerField(column_name="id", unique=True, primary_key=True)
    name = CharField(column_name="name", max_length=100)
    url_book = CharField(column_name="url_book", max_length=2048)
    author = CharField(column_name="author", max_length=250)
    description = TextField(column_name="description")

    class Meta:
        table_name = "book"

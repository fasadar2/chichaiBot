from BaseModel import *
from peewee import *
from UserModel import UserModel


class RatingModel(BaseModel):
    rating_id = IntegerField(column_name="id", primary_key=True)
    user_id = ForeignKeyField(column_name="user_id", lazy_load=False, model=UserModel)
    point = IntegerField(column_name="point")

    class Meta:
        table_name = "rating"

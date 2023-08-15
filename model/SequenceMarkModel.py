from BaseModel import *
from peewee import *
from MarkModel import *
from SequenceModel import *
class SequenceMarkModel(BaseModel):
    sequence_mark_model_id = IntegerField(column_name="id",primary_key=True)
    mark_id = ForeignKeyField(model=MarkModel,column_name="mark_id",lazy_load=False)
    sequence_id = ForeignKeyField(model = SequenceModel,column_name="sequence_id",lazy_load=False)
    chat_id = IntegerField(column_name="chat_id")
    class Meta:
        table_name = "sequence_mark"

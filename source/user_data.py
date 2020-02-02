
from peewee import *

db = SqliteDatabase('../save_data/food.db')

class Ingredient(Model):
    name = CharField(max_length=255)
    isle = CharField(max_length=50)
    price = IntegerField(default = 0)

    class Meta:
        database = db


def initalize():
    """Create database if it does not exits"""
    db.connect()
    db.create_tables([Ingredient], safe = True)
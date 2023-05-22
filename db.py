from peewee import *

db = SqliteDatabase('spot.sqlite')

class Image(Model):
    date = TimestampField()
    camera_id = IntegerField()
    image_url = CharField(null=True)

    class Meta:
        database = db

def create_tables():
    with db:
        db.create_tables([Image])
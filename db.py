from peewee import *

db = SqliteDatabase('spot.sqlite')

class Image(Model):
    """
    Usando el orm peewee, se crea esta clase la cual contiene los datos de la tabla Image
    Parametros:
        - date
        - camera_id
        - image_url
    """
    date = TimestampField()
    camera_id = IntegerField()
    image_url = CharField(null=True)

    class Meta:
        database = db

def create_tables():
    """
    El metodo permite crear las tablas requeridas en el motor de base de datos configurado
    """
    with db:
        db.create_tables([Image])
from peewee import *

db = PostgresqlDatabase("postgresql://neondb_owner:npg_zBZyG6Ci4SgD@ep-broad-butterfly-al7dsrcj-pooler.c-3.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")

class Todo(Model):
    title = CharField(max_length=255)
    completed = BooleanField(default=False)

    class Meta:
        database = db

db.connect()
db.create_tables([Todo])
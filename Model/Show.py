import peewee
from Model.Database import db
import logging
logger=logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

TITLE_LENGTH = 45

class Show(peewee.Model):
    traktid = peewee.PrimaryKeyField()
    tvdbid = peewee.IntegerField(null=True)
    imdbid = peewee.CharField(null=True, max_length=11)
    tmdbid = peewee.IntegerField(null=True)
    tvrageid = peewee.IntegerField(null=True)
    title = peewee.CharField(null=True, max_length=TITLE_LENGTH)
    year = peewee.IntegerField(null=True)

    class Meta:
        db_table = "show"
        database = db
    
    @staticmethod
    def getDummyShow():
        s = Show()
        s.title = "Miguel Lopes"
        s.year = 1991
        s.traktid = 8888888
        s.tmdbid = 10001
        s.tvdbid = 100001
        s.tvrageid = 10001
        s.imdbid = "aa0000001"
        s.type = "show"
        s.season = 3
        s.episode = 15
        return(s)


class Episode(peewee.Model):
    show = peewee.ForeignKeyField(Show, backref="episodes")
    season = peewee.IntegerField()
    episode = peewee.IntegerField()
    downloaded = peewee.BooleanField()

    class Meta:
        db_table = "episodes"
        database = db

tables = [Show, Episode]
db.create_tables(tables, safe=True)
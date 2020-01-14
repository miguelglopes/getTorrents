import peewee
from config.Common import config

db = peewee.MySQLDatabase(
    config["database"]["db"],
    user=config["database"]["user"],
    password=config["database"]["pwd"],
    host=config["database"]["host"],
    port=config["database"]["port"],
)

db.connect()


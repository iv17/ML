import peewee
from peewee import MySQLDatabase

db = MySQLDatabase('dates', user='root', passwd='')


class Date(peewee.Model):
    # match - 0/1
    match = peewee.IntegerField()
    # Partner 1
    # Attractive
    attr_1 = peewee.IntegerField()
    # Interest
    shar_1 = peewee.IntegerField()
    # Ambitious
    amb_1 = peewee.IntegerField()
    # Fun
    fun_1 = peewee.IntegerField()
    # Intelligent
    intel_1 = peewee.IntegerField()
    # Sincere
    sinc_1 = peewee.IntegerField()

    # Partner 2

    # Attractive
    attr_2 = peewee.IntegerField()
    # Interest
    shar_2 = peewee.IntegerField()
    # Ambitious
    amb_2 = peewee.IntegerField()
    # Fun
    fun_2 = peewee.IntegerField()
    # Intelligent
    intel_2 = peewee.IntegerField()
    # Sincere
    sinc_2 = peewee.IntegerField()

    class Meta:
        database = db

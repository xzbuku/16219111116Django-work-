# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movietreu(models.Model):
    mname = models.TextField()
    content = models.TextField()
    data = models.DateField()
    actor = models.CharField(max_length=20)
    imgsrc = models.TextField()

    class Meta:
        managed = False
        db_table = 'movietreu'


class Phone(models.Model):
    title = models.TextField()
    imgsrc = models.TextField()
    price = models.CharField(max_length=20)
    delete = models.IntegerField(db_column='Delete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phone'


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    introfuce = models.TextField()

    class Meta:
        managed = False
        db_table = 'student'

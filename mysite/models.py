# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=10)
    dept_code = models.CharField(unique=True, max_length=5)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """Java toString 方法"""
        return self.name

    class Meta:
        managed = False
        db_table = 'dept'


class Employee(models.Model):
    employee_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=10)
    age = models.IntegerField()
    gender = models.IntegerField()
    create_time= models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # ManyToOne
    dept = models.ForeignKey(Dept)

    def __unicode__(self):
        """Java toString 方法"""
        return self.name

    class Meta:
        managed = False
        db_table = 'employee'

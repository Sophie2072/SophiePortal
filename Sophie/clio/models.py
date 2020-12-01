from django.db import models
from django.utils import timezone


class Staff(models.Model):
    forename = models.CharField(max_length=150)
    surename = models.CharField(max_length=150)
    number = models.CharField("Mobile Number", max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200, default="")

    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Member(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    forename = models.CharField(max_length=150, default="")
    surename = models.CharField(max_length=150,default="")
    number = models.CharField("Mobile Number", max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200, default="")
    balance = models.BigIntegerField(default=0)
    data_joined = models.DateField(default=True)
    notes = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name + " " + self.number


class Card(models.Model):
    category = models.CharField(max_length=150)
    value = models.BigIntegerField(default=0)
    cost = models.BigIntegerField(default=0)
    balance = models.BigIntegerField(default=0)
    start = models.DateTimeField("start time", default="")
    end = models.DateTimeField("end time", default="")
    notes = models.CharField(max_length=300, default="")
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.category


class Team(models.Model):
    short_name = models.CharField(max_length=150)
    long_name = models.CharField(max_length=150)
    is_hourly = models.BooleanField(default=True)


class Role(models.Model):
    title = models.CharField(max_length=150)
from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField(default=0, max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=200)


class Member(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0, max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=200)

class Card(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.CharField()
    date = models.DateTimeField('date published')


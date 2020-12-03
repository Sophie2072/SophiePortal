from django.db import models
from django.utils import timezone


class Staff(models.Model):
    forename = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    number = models.CharField("Mobile Number", max_length=15)
    email = models.EmailField("Email")
    address = models.CharField(max_length=200, default="")
    team = models.ForeignKey(
        "Team", on_delete=models.SET_NULL, null=True, related_name="staff"
    )
    role = models.ForeignKey(
        "Role", on_delete=models.SET_NULL, null=True, related_name="staff"
    )
    is_active = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Member(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    forename = models.CharField(max_length=150, default="")
    surname = models.CharField(max_length=150, default="")
    number = models.CharField("Mobile Number", max_length=15)
    email = models.EmailField("Email")
    address = models.CharField(max_length=200, default="")
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    first_card = models.ForeignKey(
        "Card", on_delete=models.SET_NULL, null=True, related_name="first_card"
    )
    second_card = models.ForeignKey(
        "Card", on_delete=models.SET_NULL, null=True, related_name="second_card"
    )
    data_joined = models.DateField(default=True)
    notes = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name + " " + self.number


class Card(models.Model):
    category = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    start = models.DateTimeField("Start Time", default="")
    end = models.DateTimeField("End Time", default="")
    notes = models.CharField(max_length=300, default="")
    date = models.DateTimeField("Date Published")

    def __str__(self):
        return self.category


class Team(models.Model):
    short_name = models.CharField(max_length=150)
    long_name = models.CharField(max_length=150)
    is_hourly = models.BooleanField(default=False)


class Role(models.Model):
    title = models.CharField(max_length=150)

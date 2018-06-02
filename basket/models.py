from django.db import models
from basket.defines import POSITION_PLAYER_CHOICES
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Team(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos')
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    height = models.PositiveIntegerField(help_text="Altura en cm")
    weight = models.PositiveIntegerField(help_text="Peso en gramos")
    picture = models.ImageField(upload_to='basket')
    position = models.CharField(max_length=60, choices=POSITION_PLAYER_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    rut = models.CharField(max_length=8)
    dv = models.CharField(max_length=1)

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)

    def __str__(self):
        return self.name


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    nickname = models.CharField(max_length=120)

    rut = models.CharField(max_length=8)
    dv = models.CharField(max_length=1)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)
    def __str__(self):
        return self.name

class Payroll(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def _str_(self):
        return self.name
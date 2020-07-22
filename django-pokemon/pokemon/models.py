from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type_1 = models.CharField(max_length=100)
    type_2 = models.CharField(max_length=100, blank=True)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    legendary = models.BooleanField()
    
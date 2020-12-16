from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Pokemon(models.Model):

    Uid =  models.CharField( max_length = 10000, blank = True)
    name = models.CharField( max_length = 100, blank = True)
    type = models.CharField( max_length = 100, blank = True)
    level = models.IntegerField(
        validators=[
        MaxValueValidator(100000) ,
        MinValueValidator(0)],
        blank = False ,
        null = False ,
        default= 0,
    )
    evolution_level =models.IntegerField(
        validators=[
        MaxValueValidator(100000) ,
        MinValueValidator(0)],
        blank = False ,
        null = False ,
        default= 0,
    )
    image = models.CharField( max_length = 10000, blank = True)
    evolution_to = models.CharField( max_length = 100, blank = True)
    abilities = models.CharField( max_length = 100, blank = True)

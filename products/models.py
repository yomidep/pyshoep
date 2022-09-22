from django.db import models


class Product(models.Model):
    Name = models.CharField(max_length = 255)
    Price = models.FloatField()
    Stock = models.IntegerField()
    Image_url = models.CharField(max_length = 2083)    

class Offers(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    discount = models.FloatField()
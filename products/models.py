from django.db import models
from PIL import Image 


class Product(models.Model):
    Name = models.CharField(max_length = 255)
    Price = models.FloatField()
    Stock = models.IntegerField()
    Image = models.ImageField(null = True, blank = True, upload_to = 'Images')    
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url

class Offers(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    discount = models.FloatField()
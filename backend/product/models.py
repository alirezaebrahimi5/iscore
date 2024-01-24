from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Product(models.Model):
    title = models.CharField()
    img = models.ImageField(upload_to='product/')
    slug = models.SlugField()
    price = models.FloatField()
    description = models.CharField()
    capacity = models.PositiveBigIntegerField()


class Product_by_Sales_Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

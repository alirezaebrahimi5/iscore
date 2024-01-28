from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class ProductType:
    PRODUCT = 1
    SERVICE = 2
    
    Product_Type = (
        ('محصولات', PRODUCT),
        ('خدمات', SERVICE),
    )


class Product(models.Model):
    title       = models.CharField(max_length=144)
    img         = models.ImageField(upload_to='product/')
    slug        = models.SlugField(allow_unicode=True)
    price       = models.FloatField()
    description = models.CharField(max_length=400)
    capacity    = models.PositiveBigIntegerField()
    prod_type   = models.PositiveSmallIntegerField(choices=ProductType.Product_Type, default=1)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.title} {self.price} {self.capacity} {self.is_verified} {self.prod_type}"

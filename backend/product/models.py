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
    title       = models.CharField(max_length=144, unique=True, primary_key=True, verbose_name='')
    img         = models.ImageField(upload_to='product/', verbose_name='')
    slug        = models.SlugField(allow_unicode=True, verbose_name='')
    price       = models.FloatField(verbose_name='')
    description = models.CharField(max_length=400, verbose_name='')
    capacity    = models.PositiveBigIntegerField(verbose_name='')
    prod_type   = models.PositiveSmallIntegerField(choices=ProductType.Product_Type, default=1, verbose_name='')
    is_verified = models.BooleanField(default=False, verbose_name='')
    is_existed = models.BooleanField(default=True, verbose_name='')
    
    def __str__(self) -> str:
        return f"{self.title} {self.price} {self.capacity} {self.is_verified} {self.is_exisited} {self.prod_type}"


class Instance(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    img         = models.ImageField(upload_to='product/')
    slug        = models.SlugField(allow_unicode=True)
    price       = models.FloatField()
    description = models.CharField(max_length=400)
    capacity    = models.PositiveBigIntegerField()
    prod_type   = models.PositiveSmallIntegerField(choices=ProductType.Product_Type, default=1)
    
    def __str__(self) -> str:
        return f"{self.product} {self.price} {self.capacity} {self.prod_type}"


class Factor(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", verbose_name='')
    product       = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products", verbose_name='')
    purchaser     = models.CharField(max_length=50, verbose_name='')
    price         = models.FloatField(verbose_name='')
    description   = models.CharField(max_length=500, verbose_name='')
    discount      = models.FloatField(verbose_name='')
    with_check    = models.BooleanField(default=False, verbose_name='')
    check_dealine = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.user} {self.product} {self.purchaser} {self.price} {self.discount} {self.with_check}"

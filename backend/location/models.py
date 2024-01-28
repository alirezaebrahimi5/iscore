from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


User = settings.AUTH_USER_MODEL


class LocationType:
    PRODUCT = 1
    SERVICE = 2
    
    Location_Type = (
        ('محصولات', PRODUCT),
        ('خدمات', SERVICE),
    )


class UserLocation(models.Model):
    numbers     = RegexValidator(r'^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude    = models.CharField(validators=[numbers], max_length=20)
    longitude   = models.CharField(validators=[numbers], max_length=20)
    created_at  = models.DateTimeField(auto_now=True)
    
    @property
    def where_is(self):
        return '(' + str(self.latitude) + ',' + str(self.longitude) + ')'
    
    def __str__(self) -> str:
        return f"{self.user} {self.where_is}"
    
    class Meta:
        ordering = ['user']


class NewLocation(models.Model):
    numbers             = RegexValidator(r'^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    title               = models.CharField(max_length=144)
    lat                 = models.CharField(validators=[numbers], max_length=20)
    log                 = models.CharField(validators=[numbers], max_length=20)
    address             = models.CharField(max_length=4096)
    location_type       = models.PositiveSmallIntegerField(choices=LocationType.Location_Type, default=1)
    saleManagerVerified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.user} {self.title} {self.saleManagerVerified}"

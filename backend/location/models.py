from django.conf import settings

from mongoengine import DynamicDocument, fields, Document


User = settings.AUTH_USER_MODEL


class LocationType:
    PRODUCT = 1
    SERVICE = 2
    
    Location_Type = (
        ('محصولات', PRODUCT),
        ('خدمات', SERVICE),
    )


class UserLocation(DynamicDocument):
    # TODO : where is on_delete option?
    user      = fields.ReferenceField(User)
    latitude  = fields.StringField(regex=r'^[0-9a]*$', max_length=11)
    longitude = fields.StringField(regex=r'^[0-9a]*$', max_length=11)
    
    def __str__(self):
        return f"{self.user}"


class NewLocation(DynamicDocument):
    title     = fields.StringField(regex=r'^[0-9a-zA-Z]*$', max_length=140)
    latitude  = fields.StringField(regex=r'^[0-9a]*$', max_length=11)
    longitude = fields.StringField(regex=r'^[0-9a]*$', max_length=11)
    is_verified = fields.BooleanField(default=False)
    type_of     = fields.StringField(choices=LocationType.Location_Type, default=1)

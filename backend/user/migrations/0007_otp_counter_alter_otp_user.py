# Generated by Django 4.2.10 on 2024-02-23 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_identificationcode_user_nid'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='counter',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='otp',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_otp', to=settings.AUTH_USER_MODEL),
        ),
    ]

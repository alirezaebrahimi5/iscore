from celery import shared_task
from django.utils.timezone import timedelta

from .models import *


@shared_task
def dailyScore(user):
    pass

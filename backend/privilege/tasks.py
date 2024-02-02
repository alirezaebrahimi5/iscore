from celery import shared_task
from django.utils.timezone import timedelta
from django.conf import settings

from .models import *


User = settings.AUTH_USER_MODEL


@shared_task
def dailyScore():
    users = User.objects.all()
    for user in users:
        k = 0
        all_user_times = UserTime.objects.get(user=user)
        for t in all_user_times:
            k = k + t.spent_time
        return k

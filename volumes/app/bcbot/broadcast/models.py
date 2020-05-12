from django.db import models

# Create your models here.
from datetime import datetime, timedelta, timezone
import calendar

JST = timezone(timedelta(hours=+9), 'JST')
MONTHS = [(x, x) for x in range(1, 13)]
HOURS = [(x, x) for x in range(0, 24)]
MINUTES = [(x, x) for x in range(0, 60)]

class Register(models.Model):
    NOW = datetime.now(JST)
    YEARS = [(x, x) for x in range(NOW.year, NOW.year + 10)]
    DAYS = [(x, x) for x in range(1, calendar.monthrange(NOW.year, NOW.month)[1])]
    Broadcast_messages = models.TextField(blank=True)
    Years = models.IntegerField(choices=YEARS, default=NOW.year)
    Months = models.IntegerField(choices=MONTHS, default=NOW.month)
    Days = models.IntegerField(choices=DAYS, default=NOW.day)
    Hours = models.IntegerField(choices=HOURS, default=NOW.hour)
    Minutes = models.IntegerField(choices=MINUTES, default=NOW.minute)

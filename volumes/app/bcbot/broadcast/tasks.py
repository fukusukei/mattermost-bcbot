from logging import getLogger
from bcbot.celery import app
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import pytz
from .announce import getchannels, get_star, broadcast

logger = getLogger(__name__)


@app.task
def scheduled_broadcast():
    broadcast(get_star(getchannels()))


@app.task
def Broadcast_Entrytasks(Years, Months, Days, Hours, Minutes):
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=Minutes,
        hour=Hours,
        day_of_week='*',
        day_of_month=Days,
        month_of_year=Months,
        timezone=pytz.timezone('Asia/Tokyo')
    )

    PeriodicTask.objects.create(
        crontab=schedule,
        name='Importing contacts',
        task='broadcast.tasks.scheduled_broadcast',
    )

    PeriodicTask.save()
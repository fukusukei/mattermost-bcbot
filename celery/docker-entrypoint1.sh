#!/bin/ash

echo "Run mode ${CELERY_RUNMODE}"

if [ ${CELERY_RUNMODE} = "worker" ] ; then
  echo "Run mode ${CELERY_RUNMODE}"
  #sh -c "wait-for celery-broker:6379 && wait-for app:8000 -- DJANGO_SETTINGS_MODULE=bcbot.settings celery -A bcbot worker -l info"
  celery -A bcbot worker -l info
elif [ ${CELERY_RUNMODE} = "beat" ] ; then
  echo "Run mode ${CELERY_RUNMODE}"
  #sh -c "wait-for celery-broker:6379 && wait-for app:8000 --  DJANGO_SETTINGS_MODULE=bcbot.settings celery -A bcbot beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile="
  celery -A bcbot beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile=
fi

history -c
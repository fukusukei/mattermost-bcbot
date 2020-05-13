#!/bin/ash

echo "Run mode ${CELERY_RUNMODE}"

if [ "${CELERY_RUNMODE}" = "worker" ]; then
  ash -c "DJANGO_SETTINGS_MODULE=bcbot.settings celery -A bcbot worker -l info"
elif [ "${CELERY_RUNMODE}" = "beat" ]; then
  ash -c "DJANGO_SETTINGS_MODULE=bcbot.settings celery -A bcbot beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile="
else
  echo "Invaild Mode"
fi

history -c
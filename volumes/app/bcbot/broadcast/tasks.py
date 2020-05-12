from celery import shared_task
import time
from logging import getLogger

logger = getLogger(__name__)

@shared_task
def add(x1, x2):
	time.sleep(10)
	y = x1 + x2

	logger.error('result:')
	return y
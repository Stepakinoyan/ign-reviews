from celery import Celery
from celery.schedules import crontab

from app.config import settings

celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=[
        "app.dao.dao",
        "app.tasks.scheduled"
    ]
)

celery.conf.beat_schedule = {
    "prepare-db-every-day": {
        "task": "prepare_db_every_day",
        "schedule": crontab(minute=0, hour=0)
    }
}
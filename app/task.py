import os
from time import sleep

from celery.app import Celery

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")

app = Celery(__name__, broker=redis_url, backend=redis_url)


@app.task
def dummy_task(name="Bob") -> str:
    sleep(10)
    return f"Hello {name}!"

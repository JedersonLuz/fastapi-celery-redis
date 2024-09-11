from celery.result import AsyncResult
from fastapi import FastAPI
from pydantic import BaseModel

from app import task

app = FastAPI()


class TaskOut(BaseModel):
    id: str
    status: str


@app.get("/start")
def start(name: str) -> TaskOut:
    r = task.dummy_task.delay(name=name)
    return _to_task_out(r)


@app.get("/status")
def status(task_id: str) -> TaskOut:
    r = task.app.AsyncResult(task_id)
    return _to_task_out(r)


def _to_task_out(r: AsyncResult) -> TaskOut:
    return TaskOut(id=r.task_id, status=r.status)

from celery.result import AsyncResult
from fastapi import FastAPI
from pydantic import BaseModel

from app import task

app = FastAPI()


class TaskIn(BaseModel):
    name: str


class TaskOut(BaseModel):
    id: str
    status: str
    result: str | None = None


@app.post("/start")
def start(task_in: TaskIn) -> TaskOut:
    r = task.dummy_task.delay(name=task_in.name)
    return _to_task_out(r)


@app.get("/result/{task_id}")
def result(task_id: str) -> TaskOut:
    r = task.app.AsyncResult(task_id)
    return _to_task_out(r)


def _to_task_out(r: AsyncResult) -> TaskOut:
    return TaskOut(id=r.task_id, status=r.status, result=r.result)

from fastapi import FastAPI
import uvicorn
import redis
from rq import Queue
from enum import Enum
from tasks import background_task
from rq.job import Job

app = FastAPI()

r = redis.Redis()
q = Queue(connection=r)


class Status(str, Enum):
    accepted = "accepted"
    running = "running"
    error = "error"
    complete = "complete"
    not_found = "not_found"


status_map_dict = {
    "queued": Status.accepted,
    "started": Status.running,
    "failed": Status.error,
    "finished": Status.complete,
}


@app.get("/task/{job_id}")
async def get_status(job_id: str):

    status: Status = Status.not_found

    job: Job = q.fetch_job(job_id)
    if job:
        status = status_map_dict[job.get_status(job_id)]

    return {"status": status}


@app.get("/task", status_code=201)
async def add_task():

    job = q.enqueue(background_task, result_ttl=1200)
    return {"task": job.id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

import asyncio
from fastapi import FastAPI
from redis import Redis
from loguru import logger

from .lock import RedisLock


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/lock")
async def lock(i: int):
    redis = Redis(host="localhost", port=6379, db=8)
    logger.info(f"enter lock {i}")
    with RedisLock(redis, "test_lock", blocking=True, blocking_timeout=5) as lock:
        logger.info(f"lock {i}")
        await asyncio.sleep(0.1)
        logger.info(f"leave lock {i}")
        print(lock)
    return {"message": f"Lock ok {i}"}

import asyncio
import aiohttp
from loguru import logger

async def main():
    async with aiohttp.ClientSession() as session:
        reqs = []
        for i in range(10):
            logger.info(f"start {i}")
            req = session.get("http://localhost:8000/lock", params={"i": i})
            reqs.append(req)
            logger.info(f"req {i} send")
        await asyncio.gather(*reqs)
        logger.info("end")


if __name__ == "__main__":
    asyncio.run(main())

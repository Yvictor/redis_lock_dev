from types import TracebackType
from typing import Optional, Type
from redis.lock import Lock as _RedisLock


class RedisLock(_RedisLock):
    def __enter__(self) -> "RedisLock":
        self.acquire()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if self.owned():
            self.release()

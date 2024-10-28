from redis.asyncio import Redis
from fastapi import FastAPI
from os import getenv
from typing import Union

# region Singleton Accessors

async def get_redis() -> Redis:
    """Retrieves the redis singleton"""
    return await DelveRedis.get_redis()

# endregion

# region Singleton Definition

class DelveRedis(object):

    app : FastAPI
    redis_client : Union[Redis, None]

    def _register_app_events(self) -> None:
        """Registers the event handlers for the starlette app so that the redis client exists only when it needs to"""

        # Add an event handler to initialize the database on app startup
        self.app.add_event_handler(
            "startup",
            self._init_redis
        )

        # and another to shut the database down.
        self.app.add_event_handler(
            "shutdown",
            self._close_redis
        )

    async def _init_redis(self) -> None:
        """A hook to initialize the redis client instance and set the class attr for the singleton"""
        
        tmp = await Redis(
            host=getenv('REDIS_HOST'),
            port=getenv('REDIS_PORT'),
            password=getenv("REDIS_PASS")
        )

        try:
            setattr(
                self.__class__, 
                'redis_client', 
                tmp
            )
        except Exception as err:
            raise err

    async def _close_redis(self) -> None:
        """A hook to shut the redis client down when the app needs to shut down"""
        
        redis_client : Union[Redis, None] = getattr(self.__class__, "redis_client", None)

        # Redis has already been closed
        if redis_client is None:
            return
        
        await redis_client.close() # "garceful" shutdown (yes, i said garceful)
        setattr(self.__class__, "redis_client", None)

    @classmethod
    def using_app(cls, app : FastAPI) -> None:
        """Indicate what app the redis client needs to hook into"""
        singleton_obj = cls()
        singleton_obj.app = app
        singleton_obj._register_app_events()

    @classmethod
    async def get_redis(cls) -> Redis:
        """Returns the redis client object"""
        return getattr(cls, "redis_client")

# endregion
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase
from fastapi import FastAPI
from os import getenv
from typing import Union

# region Singleton Accessors

async def get_database() -> AgnosticDatabase:
    """Retrieves the default database using the database singleton"""
    return await Database.get_database()

async def get_client() -> AgnosticClient:
    """Retrieves the motor client from the singleton"""
    return await Database.get_client()

# endregion

# region Singleton Definition

class Database(object):

    app : FastAPI
    db_instance : Union[AsyncIOMotorClient, None]

    def _register_app_events(self) -> None:
        """Registers the event handlers for the starlette app so that the database exists only when it needs to"""

        # Add an event handler to initialize the database on app startup
        self.app.add_event_handler(
            "startup",
            self._init_database
        )

        # and another to shut the database down.
        self.app.add_event_handler(
            "shutdown",
            self._shutdown_database
        )

    async def _init_database(self) -> None:
        """A hook to initialize the database instance and set the class attr for the singleton"""
        
        try:
            setattr(
                self.__class__, 
                'db_instance', 
                AsyncIOMotorClient(
                    getenv("MONGODB_URI")
                )
            )
        except Exception as err:
            raise err

    async def _shutdown_database(self) -> None:
        """A hook to shut the database down when the app needs to shut down"""
        
        db_instance : Union[AsyncIOMotorClient, None] = getattr(self.__class__, "db_instance", None)

        # Database has already been shut down
        if db_instance is None:
            return
        
        db_instance.close() # "garceful" shutdown (yes, i said garceful)
        setattr(self.__class__, "db_instance", None)

    @classmethod
    def using_app(cls, app : FastAPI) -> None:
        """Indicate what app the database needs to hook into"""
        singleton_obj = cls()
        singleton_obj.app = app
        singleton_obj._register_app_events()

    @classmethod
    async def get_client(cls) -> AgnosticClient:
        """Returns the motor client object"""
        return getattr(cls, "db_instance")

    @classmethod
    async def get_database(cls) -> AgnosticDatabase:
        """Returns the motor database object, referencing the .env for the database name"""
        client = await cls.get_client()
        return client.get_database(
            getenv("MONGODB_DATABASE", "delve")
        )

# endregion
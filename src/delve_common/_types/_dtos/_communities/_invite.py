from pydantic import BaseModel, Field, computed_field
from datetime import UTC, datetime, timedelta
from typing import Union

from .._user import User

class Invite(BaseModel):

    community_id : str
    invite_code : str
    author : User

    valid_duration : Union[timedelta, None] # if none, infinite duration

    # region metrics
    uses : int = Field(default=0)
    # endregion

    # region metadata
    created_at : datetime = Field(
        default_factory=datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=datetime.now(tz=UTC))
    # endregion

    # region helper properties
    @computed_field
    @property
    def expires_at(self) -> Union[datetime, None]:

        if self.valid_duration is None:
            return None
        
        return self.created_at + self.valid_duration
    
    @computed_field
    @property
    def is_expired(self) -> bool:

        if self.expires_at is None:
            return False
        
        return self.expires_at <= datetime.now(tz=UTC)
    # endregion
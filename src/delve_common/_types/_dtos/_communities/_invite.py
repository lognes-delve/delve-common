from pydantic import BaseModel, Field, computed_field
from datetime import UTC, datetime, timedelta
from typing import Union

class Invite(BaseModel):

    id : str
    community_id : str
    invite_code : str
    author_id : str

    valid_duration : Union[timedelta, None] # if none, infinite duration

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion
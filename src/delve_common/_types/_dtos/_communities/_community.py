from datetime import UTC, datetime
from pydantic import BaseModel, Field
from typing import List
from ._channel import Channel
from ._role import Role

class Community(BaseModel):

    id : str
    name : str
    owner_id : str

    channels : List[Channel] = Field(default=[])
    roles : List[Role] = Field(default=[])

    # region metrics
    
    member_count : int = Field(default=1)
    channel_count : int = Field(default=0)
    role_count : int = Field(default=0)

    # endregion

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion

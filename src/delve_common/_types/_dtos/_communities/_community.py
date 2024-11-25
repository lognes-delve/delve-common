from datetime import UTC, datetime
from pydantic import BaseModel, Field
from typing import List
from ._role import Role

class Community(BaseModel):

    id : str
    name : str
    owner_id : str

    channel_ids : List[str] = Field(default=[])
    roles : List[Role] = Field(default=[])

    flags : List[str] = Field(default=[])

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion

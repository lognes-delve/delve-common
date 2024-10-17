from datetime import UTC, datetime
from pydantic import BaseModel, Field
from typing import List, Union

from .._user import User
from ._role import Role

class Member(BaseModel):

    user : User
    community_id : str

    roles : List[Role] = Field(default=[])
    nickname : Union[str, None] = Field(default=None)

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion
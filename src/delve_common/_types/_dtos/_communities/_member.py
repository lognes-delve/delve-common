from datetime import UTC, datetime
from pydantic import BaseModel, Field
from typing import List, Union

class Member(BaseModel):

    id : str # 1:1 with user's id
    community_id : str

    role_ids : List[str] = Field(default=[])
    nickname : Union[str, None] = Field(default=None)

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion
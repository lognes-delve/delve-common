from pydantic import BaseModel, Field
from datetime import datetime, UTC
from typing import List, Literal, Optional

VALID_STATUSES = Literal[
    "online", "away", "dnd", "invisible"
]

class User(BaseModel):
    
    id : str
    username : str

    display_name : Optional[str] = Field(default=None)
    bio : Optional[str] = Field(default=None)
    pronouns : Optional[str] = Field(default=None)

    flags : List[str] = Field(default=[])
    status : str = Field(default="online")
    last_seen : datetime = Field(default_factory=lambda: datetime(0, 0, 0, 0, 0, 0, 0, UTC))

    icon_key : Optional[str] = Field(default=None)
    icon_primary : Optional[int] = Field(default=None)
    icon_secondary : Optional[int] = Field(default=None)

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion
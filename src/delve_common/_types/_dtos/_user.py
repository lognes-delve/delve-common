from pydantic import BaseModel, Field
from datetime import datetime, UTC
from typing import Optional

class User(BaseModel):
    
    id : str
    username : str

    display_name : Optional[str] = Field(default=None)
    bio : Optional[str] = Field(default=None)
    pronouns : Optional[str] = Field(default=None)

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion
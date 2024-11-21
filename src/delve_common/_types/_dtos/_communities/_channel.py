from datetime import UTC, datetime
from typing import Dict
from pydantic import BaseModel, Field

class Channel(BaseModel):

    id : str
    community_id : str
    name : str

    # {"role_id" : {"key" : true/false, ...}, ...}
    permission_overrides : Dict[str, Dict[str, bool]] = Field(default={})

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion
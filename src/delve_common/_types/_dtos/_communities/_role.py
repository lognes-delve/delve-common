from datetime import UTC, datetime
from pydantic import BaseModel, Field
from typing import Dict, Optional

class Role(BaseModel):

    id : str
    name : str
    colour : Optional[int] = Field(default=None)
    community_id : str

    permisson_overrides : Dict[str, bool] = Field(default={})

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion
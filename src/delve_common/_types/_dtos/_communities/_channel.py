from datetime import UTC, datetime
from pydantic import BaseModel, Field

class Channel(BaseModel):

    id : str
    community_id : str
    name : str

    # region metadata
    created_at : datetime = Field(
        default_factory=datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=datetime.now(tz=UTC))
    # endregion
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from typing import List, Optional

class MessageContent(BaseModel):

    text : str

class Message(BaseModel):

    id : str
    author_id : str
    channel_id : str
    community_id : str

    content : MessageContent
    mentions : Optional[List[str]] = Field(default=None)

    # region metadata
    created_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    
    edited_at : datetime = Field(
        default_factory=lambda: datetime.now(tz=UTC))
    # endregion
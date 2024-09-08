from pydantic import BaseModel, Field
from typing import Dict, Optional, Union

from ._utils import JSONSerializable

class DelveAPIExceptionModel(BaseModel):
    """A pydantic model for an exception, probably more useful in websocket scenarios"""

    status_code : int
    identifier : str
    detail : Optional[Union[str, None]] = Field(default=None)
    headers : Optional[Dict[str, str]] = Field(default={})
    additional_metadata : Optional[Dict[str, JSONSerializable]] = Field(default={})
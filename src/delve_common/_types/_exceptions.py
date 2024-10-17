from starlette.exceptions import HTTPException
from typing import Optional, Dict, Any
from ._models import DelveAPIExceptionModel

class DelveHTTPException(HTTPException):
    """An extension of `starlette.exceptions.HTTPException` that includes an additional field for filtering"""

    identifier : str = "delve_exception"
    additional_metadata : Dict[str, Any]

    def __init__(
            self,
            status_code: Optional[int] = 500,
            detail: str | None = None, 
            identifier : Optional[str] = None,
            headers: dict[str, str] | None = None,
            additional_metadata : Dict[str, Any] = None
        ) -> None:

        super().__init__(status_code, detail, headers)

        self.identifier = identifier
        self.additional_metadata = additional_metadata

    def to_model(self) -> DelveAPIExceptionModel:
        """Returns a serialized model of the exception"""
        return DelveAPIExceptionModel(
            status_code = self.status_code,
            identifier = self.identifier,
            detail = self.detail,
            headers = self.headers,
            additional_metadata = self.additional_metadata
        )

__all__ = [
    "DelveHTTPException"
]
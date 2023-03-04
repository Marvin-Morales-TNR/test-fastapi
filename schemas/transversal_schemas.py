from typing import Any
from pydantic import BaseModel

class ErrorGeneral(BaseModel):
    code: str
    details: str

class GeneralResponse(BaseModel):
    success: bool
    error: ErrorGeneral | None
    data: Any | None
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DataLogger(BaseModel):
    error: str | None

class Log_Response(BaseModel):
    success: bool
    info: Optional[DataLogger]

class Logging(object):
    def __init__(self, text: str, code: int) -> None:
        self.text = text
        self.default_code = code

    def save_log(self) -> Log_Response:
        try:
            with open("logs.txt", "a", encoding="utf-8") as file:
                file.write(f"{str(datetime.now())} - Log:\n")
                file.write(f"{self.text}\n\n")
                file.close()
            return Log_Response(success=True, info={"error": None})
        except OSError as err:
            return Log_Response(success=False, info={"error": err})
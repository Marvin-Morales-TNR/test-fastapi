from pydantic import BaseModel

class Auth_post_request(BaseModel):
    index: str | int
    api_key: str
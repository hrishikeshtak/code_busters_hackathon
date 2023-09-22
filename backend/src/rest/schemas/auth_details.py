from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str


class NavigatorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    role: str

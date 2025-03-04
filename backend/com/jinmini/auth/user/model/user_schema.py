from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: str
    email: str
    password: str
    name: str
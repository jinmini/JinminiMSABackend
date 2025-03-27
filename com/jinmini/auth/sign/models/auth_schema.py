from pydantic import BaseModel
from typing import Optional

class AuthSchema(BaseModel):
    success: bool
    message: str
    token: Optional[str] = None
    user_id: Optional[str] = None


class LoginSchema(BaseModel):
    email: str
    password: str


from pydantic import BaseModel
from typing import Optional

class AuthSchema(BaseModel):
    success: bool
    message: str
    token: Optional[str] = None
    user_id: Optional[str] = None

class SigninSchema(BaseModel):
    email: str
    password: str

class SigninResponseSchema(BaseModel):
    success: bool
    message: str
    token: Optional[str] = None
    refresh_token: Optional[str] = None
    user_id: Optional[str] = None

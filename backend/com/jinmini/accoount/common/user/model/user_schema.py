from pydantic import BaseModel, EmailStr

class MemberBase(BaseModel):
    user_id: str
    email: EmailStr
    name: str  

class MemberCreate(MemberBase):
    password : str

class MemberResponse(MemberBase):
    class Config:
        from_attributes = True
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    user_id: str
    email: EmailStr
    name: str  
    password: str

    class Config:
        from_attributes = True

# class MemberCreate(MemberBase):
#     password : str

# class MemberResponse(MemberBase):
#     class Config:
#         from_attributes = True
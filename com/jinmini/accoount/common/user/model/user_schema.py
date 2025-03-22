from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    user_id: str = Field(..., example=None)
    email: EmailStr = Field(..., example=None)
    name: str = Field(..., example=None)
    password: str = Field(..., example=None)

    class Config:
        from_attributes = True
        schema_extra = {
            "example": None  # 예시값 비활성화
        }

# class MemberCreate(MemberBase):
#     password : str

# class MemberResponse(MemberBase):
#     class Config:
#         from_attributes = True
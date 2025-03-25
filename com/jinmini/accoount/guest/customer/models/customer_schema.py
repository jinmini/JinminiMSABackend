from com.jinmini.accoount.common.user.model.user_schema import UserSchema

class CustomerSchema(UserSchema):
    """고객 정보 스키마"""
    
    class Config:
        from_attributes = True
        schema_extra = {
            "example": None  # 예시값 비활성화
        }


from com.jinmini.accoount.common.user.model.user_entity import UserEntity

class CustomerEntity(UserEntity):
    """
    고객 엔티티 클래스
    UserEntity를 상속받아 기본 사용자 정보를 모두 포함하며,
    customer 테이블에 관련된 추가 필드가 있다면 여기에 정의합니다.
    """
    
    def to_response(self):
        """CustomerResponse 모델에 맞는 딕셔너리로 변환하는 메서드"""
        return {
            "user_id": self.user_id,
            "email": self.email,
            "name": self.name
        }
    
    @classmethod
    def from_schema(cls, schema):
        """스키마로부터 엔티티 객체를 생성하는 클래스 메서드"""
        return cls(
            user_id=schema.user_id,
            email=schema.email,
            name=schema.name,
            password=schema.password
        )

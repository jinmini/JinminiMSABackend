from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr

Base = declarative_base()

class UserEntity(Base):
    __tablename__ = "member"

    user_id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<UserEntity(user_id='{self.user_id}', email='{self.email}', name='{self.name}')>"
    
    def to_dict(self):
        """엔티티를 딕셔너리로 변환하는 메서드"""
        return {
            "user_id": self.user_id,
            "email": self.email,
            "name": self.name,
            # password는 민감 정보이므로 반환하지 않음
        }


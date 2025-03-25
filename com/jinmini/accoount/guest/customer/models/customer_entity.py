from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema
from com.jinmini.accoount.common.user.model.user_entity import UserEntity
from typing import Dict, Any

class CustomerEntity(UserEntity):
    
    def to_response(self) -> Dict[str, Any]:
        
        return {
            "user_id": self.user_id,
            "email": self.email,
            "name": self.name
        }
    
    @classmethod
    def from_schema(cls, schema: CustomerSchema):
        
        return cls(
            user_id=schema.user_id,
            email=schema.email,
            name=schema.name,
            password=schema.password
        )

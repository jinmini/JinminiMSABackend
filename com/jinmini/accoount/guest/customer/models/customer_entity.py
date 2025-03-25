from com.jinmini.accoount.common.user.model.user_entity import UserEntity

class CustomerEntity(UserEntity):
    
    def to_response(self):
        
        return {
            "user_id": self.user_id,
            "email": self.email,
            "name": self.name
        }
    
    @classmethod
    def from_schema(cls, schema):
        
        return cls(
            user_id=schema.user_id,
            email=schema.email,
            name=schema.name,
            password=schema.password
        )

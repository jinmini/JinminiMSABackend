from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from com.jinmini.accoount.guest.customer.model.customer_schema import CustomerSchema

class CreateCustomerService(ABC):
    
    @abstractmethod
    def create(self, db: Session, new_customer: CustomerSchema):
        pass
 


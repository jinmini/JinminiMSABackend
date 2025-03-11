from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from com.jinmini.accoount.guest.customer.model.customer_schema import CustomerSchema

class UpdateCustomerService(ABC):
    
    @abstractmethod
    def update(self, db: Session, update_customer: CustomerSchema):
        pass
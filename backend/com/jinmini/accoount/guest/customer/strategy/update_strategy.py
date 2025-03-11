from com.jinmini.accoount.guest.customer.service.update_service import UpdateCustomerService
from sqlalchemy.orm import Session
from com.jinmini.accoount.guest.customer.model.customer_schema import CustomerSchema

class FullUpdateCustomerStrategy(UpdateCustomerService):
    
    def update(self, db: Session, update_customer: CustomerSchema):
        pass

class PartialUpdateCustomerStrategy(UpdateCustomerService):
    
    def update(self, db: Session, update_customer: CustomerSchema):
        pass



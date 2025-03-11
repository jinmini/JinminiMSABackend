from com.jinmini.accoount.guest.customer.repository.create_repository import DefaultCreateCustomerRepository
from com.jinmini.accoount.guest.customer.service.create_service import CreateCustomerService
from sqlalchemy.orm import Session
from com.jinmini.accoount.guest.customer.model.customer_schema import CustomerSchema

class DefaultCreateCustomerStrategy(CreateCustomerService):
    
    def create(self, db: Session, new_customer: CustomerSchema):
        customer_repo = DefaultCreateCustomerRepository(db)
        return customer_repo.create(new_customer)

class ValidatedCreateCustomerStrategy(CreateCustomerService):

    def create(self, db: Session, new_customer: CustomerSchema):
        pass


from com.jinmini.accoount.guest.customer.model.customer_entity import CustomerEntity
from com.jinmini.accoount.guest.customer.service.create_service import CreateCustomerService
from sqlalchemy.orm import Session
from com.jinmini.accoount.guest.customer.model.customer_schema import CustomerSchema

class DefaultCreateCustomerRepository(CreateCustomerService):
    
    def create(self, db: Session, new_customer: CustomerSchema):
        print("💫♾️🖥️Repository new_customer info : ", new_customer)
        db.add(CustomerEntity(
            user_id=new_customer.user_id,
            name=new_customer.name,
            email=new_customer.email,
            password=new_customer.password,
        ))

        db.commit()
        db.refresh(new_customer)
        return new_customer

class ValidatedCreateCustomerRepository(CreateCustomerService):

    def create(self, db: Session, new_customer: CustomerSchema):
        pass


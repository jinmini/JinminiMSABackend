from com.jinmini.accoount.guest.customer.service.delete_service import DeleteCustomerService
from sqlalchemy.orm import Session

class SoftDeleteCustomerStrategy(DeleteCustomerService):
    
    def delete(self, db: Session, user_id: int):
        pass

class HardDeleteCustomerStrategy(DeleteCustomerService):
    
    def delete(self, db: Session, user_id: int):
        pass

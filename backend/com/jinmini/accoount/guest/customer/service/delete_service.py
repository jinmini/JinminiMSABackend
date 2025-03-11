from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class DeleteCustomerService(ABC):
    
    @abstractmethod
    def delete(self, db: Session, user_id: int):
        pass

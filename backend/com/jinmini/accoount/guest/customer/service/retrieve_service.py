from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class RetrieveCustomerService(ABC):
    
    @abstractmethod
    async def retrieve(self, db: Session, **kwargs):
        pass

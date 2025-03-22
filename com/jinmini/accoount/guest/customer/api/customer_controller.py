from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional, Dict, Any

from com.jinmini.accoount.guest.customer.api.customer_factory import CustomerFactory
from com.jinmini.accoount.guest.customer.models.customer_action import CustomerAction
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema

class CustomerController:
    
    async def create_customer(self, db: AsyncSession, new_customer: CustomerSchema) -> Dict[str, Any]:
  
        return await CustomerFactory.create(strategy=CustomerAction.CREATE_CUSTOMER, db=db, new_customer=new_customer)

    async def get_customer_by_id(self, db: AsyncSession, user_id: str) -> Optional[Dict[str, Any]]:

        return await CustomerFactory.create(strategy=CustomerAction.GET_CUSTOMER_BY_ID, db=db, user_id=user_id)
    
    async def get_customer_list(self, db: AsyncSession) -> List[Dict[str, Any]]:

        return await CustomerFactory.create(strategy=CustomerAction.GET_ALL_CUSTOMER, db=db)
    
    async def get_all_customers(self, db: AsyncSession) -> List[Dict[str, Any]]:

        return await self.get_customer_list(db=db)

    async def update_customer(self, db: AsyncSession, updated_customer: CustomerSchema) -> Optional[Dict[str, Any]]:

        return await CustomerFactory.create(strategy=CustomerAction.UPDATE_CUSTOMER, db=db, updated_customer=updated_customer)
    
    async def delete_customer(self, db: AsyncSession, user_id: str) -> bool:

        return await CustomerFactory.create(strategy=CustomerAction.DELETE_CUSTOMER, db=db, user_id=user_id)
    

    


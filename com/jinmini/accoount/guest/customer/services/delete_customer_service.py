from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class DeleteCustomer(AbstractService):
   
   async def handle(self, db: AsyncSession, user_id: str):
      pass
   

    



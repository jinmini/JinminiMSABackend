from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class SoftDeleteRepository(AbstractService):

    async def delete(self,  db: AsyncSession, user_id: str):
        print("🚀🤖DeleteRepository user_id 정보 : ", user_id)
       
        return None

class HardDeleteRepository(AbstractService):

    async def delete(self, db: AsyncSession, user_id: str):
        pass
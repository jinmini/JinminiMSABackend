from com.jinmini.utils.creational.abstract.abstract_service import AbstractService
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.jinmini.accoount.guest.customer.storages.get_customer import get_all_customers

class GetAllCustomers(AbstractService):

    async def handle(self, **kwargs):
        db: AsyncSession = kwargs.get("db")
        try:
            async with db.begin():  # 🔥 트랜잭션 자동 관리
                customers = await get_all_customers(db)
            return customers  # ✅ 성공 시 데이터 반환
        except SQLAlchemyError as e:
            await db.rollback()  # 🔥 오류 발생 시 rollback()
            print("[ERROR] GetAllCustomers failed:", str(e))
            return {"error": "Failed to retrieve customer data."}  

class GetCustomerById(AbstractService):

    async def handle(self, db: AsyncSession, **kwargs):
        pass

class UpdateCustomer(AbstractService):
    
    async def handle(self, db: AsyncSession, **kwargs):
        pass
        
class PatchCustomer(AbstractService):
    
    async def handle(self, db: AsyncSession, **kwargs):
        pass



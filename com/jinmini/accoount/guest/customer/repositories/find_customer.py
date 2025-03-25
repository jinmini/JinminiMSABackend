from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text, select
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService
from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity

class GetAllRepository(AbstractService):

    async def handle(self, db, **kwargs):
        return await self.retrieve(db, **kwargs)

    async def retrieve(self, db: AsyncSession, **kwargs):
        print("💯🌈 GetAllRepository 로 진입함:")
        try:
            # SQLAlchemy ORM 쿼리 사용
            query = select(CustomerEntity)
            result = await db.execute(query)
            customer_entities = result.scalars().all()
            
            print(f"💯🌈 데이터 조회 결과: {len(customer_entities)}개의 고객 정보")
            
            # 엔티티를 응답 형식으로 변환
            customers = [
                {
                    "user_id": customer.user_id,
                    "email": customer.email,
                    "name": customer.name
                }
                for customer in customer_entities
            ]
            
            return customers
        except Exception as e:
            print("⚠️ 데이터 조회 중 오류 발생:", str(e))
            return {"error": "데이터 조회 중 오류가 발생했습니다."}
  

class GetDetailRepository(AbstractService):

    async def handle(self, db, **kwargs):
        user_id = kwargs.get("user_id")
        if not user_id:
            return {"error": "user_id is required"}
        return await self.retrieve(db, user_id)

    async def retrieve(self, db: AsyncSession, user_id: str):
        # 상세 조회 로직 구현
        try:
            # SQLAlchemy ORM 쿼리 사용
            query = select(CustomerEntity).where(CustomerEntity.user_id == user_id)
            result = await db.execute(query)
            customer = result.scalars().first()
            
            if not customer:
                return {"error": "User not found"}
                
            return {
                "user_id": customer.user_id,
                "email": customer.email,
                "name": customer.name
            }
        except Exception as e:
            print("⚠️ 데이터 조회 중 오류 발생:", str(e))
            return {"error": "데이터 조회 중 오류가 발생했습니다."}

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema


async def get_all_customers(db: AsyncSession):
    query = text("SELECT * FROM member")
    try:
            result = await db.execute(query)
            records = result.fetchall()
            return [dict(record._mapping) for record in records]
    except SQLAlchemyError as e:
        print("⚠️ 데이터 조회 중 오류 발생:", str(e))
        raise e



async def get_customer_by_id(self, db: AsyncSession, user_id: str):
    pass
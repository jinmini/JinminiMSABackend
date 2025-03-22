from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from typing import List, Optional, Any

async def get_all_customers(db: AsyncSession) -> List[CustomerEntity]:

    query = select(CustomerEntity)
    result = await db.execute(query)
    return result.scalars().all()

async def get_customer_by_id(db: AsyncSession, user_id: str) -> Optional[CustomerEntity]:
    
    query = select(CustomerEntity).where(CustomerEntity.user_id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()
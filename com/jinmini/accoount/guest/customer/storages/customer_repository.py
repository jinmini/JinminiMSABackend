from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List, Optional

from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema

class CustomerRepository:
    """고객 데이터 액세스를 위한 레포지토리 클래스"""
    
    @staticmethod
    async def create_customer(db: AsyncSession, new_customer: CustomerSchema) -> CustomerEntity:
        """
        새 고객을 생성하고 저장합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            new_customer: 고객 생성 데이터가 포함된 스키마
            
        Returns:
            생성된 고객 엔티티
        """
        # 엔티티 생성
        customer_entity = CustomerEntity.from_schema(new_customer)
        
        # 세션에 추가 및 플러시
        db.add(customer_entity)
        await db.flush()
        
        return customer_entity
    
    @staticmethod
    async def get_all_customers(db: AsyncSession) -> List[CustomerEntity]:
        """
        모든 고객 목록을 조회합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            
        Returns:
            고객 엔티티 목록
        """
        query = select(CustomerEntity)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def get_customer_by_id(db: AsyncSession, user_id: str) -> Optional[CustomerEntity]:
        """
        사용자 ID로 고객을 조회합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            user_id: 조회할 고객의 ID
            
        Returns:
            찾은 고객 엔티티 또는 None
        """
        query = select(CustomerEntity).where(CustomerEntity.user_id == user_id)
        result = await db.execute(query)
        return result.scalars().first()
    
    @staticmethod
    async def update_customer(db: AsyncSession, updated_customer: CustomerSchema) -> Optional[CustomerEntity]:
        """
        고객 정보를 업데이트합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            updated_customer: 업데이트할 고객 데이터
            
        Returns:
            업데이트된 고객 엔티티 또는 None
        """
        # 업데이트할 고객 조회
        query = select(CustomerEntity).where(CustomerEntity.user_id == updated_customer.user_id)
        result = await db.execute(query)
        customer = result.scalars().first()
        
        if not customer:
            return None
        
        # 필드 업데이트
        customer.name = updated_customer.name
        customer.email = updated_customer.email
        if updated_customer.password:
            customer.password = updated_customer.password
            
        await db.flush()
        return customer
    
    @staticmethod
    async def delete_customer(db: AsyncSession, user_id: str) -> bool:
        """
        고객을 삭제합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            user_id: 삭제할 고객의 ID
            
        Returns:
            삭제 성공 여부
        """
        query = delete(CustomerEntity).where(CustomerEntity.user_id == user_id)
        result = await db.execute(query)
        return result.rowcount > 0 
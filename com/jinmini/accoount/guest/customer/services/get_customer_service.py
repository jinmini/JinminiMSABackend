from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional, Dict, Any

from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from com.jinmini.accoount.guest.customer.storages.customer_repository import CustomerRepository
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class GetAllCustomers(AbstractService):
    """모든 고객 목록을 조회하는 서비스 클래스"""
    
    async def handle(self, **kwargs) -> List[Dict[str, Any]]:
        """
        모든 고객 목록을 조회합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            
        Returns:
            고객 정보 딕셔너리 목록
        """
        db: AsyncSession = kwargs.get("db")
        
        # 모든 고객 조회
        customers = await CustomerRepository.get_all_customers(db)
        
        # 엔티티를 응답 형식으로 변환
        return [customer.to_response() for customer in customers]

class GetCustomerById(AbstractService):
    """ID로 고객을 조회하는 서비스 클래스"""
    
    async def handle(self, **kwargs) -> Optional[Dict[str, Any]]:
        """
        사용자 ID로 고객을 조회합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            user_id: 조회할 고객의 ID
            
        Returns:
            고객 정보 딕셔너리 또는 None
        """
        db: AsyncSession = kwargs.get("db")
        user_id: str = kwargs.get("user_id")
        
        # ID로 고객 조회
        customer = await CustomerRepository.get_customer_by_id(db, user_id)
        
        # 고객이 없으면 None 반환
        if not customer:
            return None
            
        # 엔티티를 응답 형식으로 변환
        return customer.to_response()

class UpdateCustomer(AbstractService):
    """고객 정보를 업데이트하는 서비스 클래스"""
    
    async def handle(self, **kwargs) -> Optional[Dict[str, Any]]:
        """
        고객 정보를 업데이트합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            updated_customer: 업데이트할 고객 데이터
            
        Returns:
            업데이트된 고객 정보 딕셔너리 또는 None
        """
        db: AsyncSession = kwargs.get("db")
        updated_customer = kwargs.get("updated_customer")
        
        try:
            async with db.begin():
                # 고객 정보 업데이트
                customer = await CustomerRepository.update_customer(db, updated_customer)
                
                # 고객이 없으면 None 반환
                if not customer:
                    return None
                
                # 엔티티를 응답 형식으로 변환
                return customer.to_response()
        except Exception as e:
            print(f"고객 정보 업데이트 중 오류 발생: {str(e)}")
            raise e

class DeleteCustomer(AbstractService):
    """고객을 삭제하는 서비스 클래스"""
    
    async def handle(self, **kwargs) -> bool:
        """
        고객을 삭제합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            user_id: 삭제할 고객의 ID
            
        Returns:
            삭제 성공 여부
        """
        db: AsyncSession = kwargs.get("db")
        user_id: str = kwargs.get("user_id")
        
        try:
            async with db.begin():
                # 고객 삭제
                return await CustomerRepository.delete_customer(db, user_id)
        except Exception as e:
            print(f"고객 삭제 중 오류 발생: {str(e)}")
            raise e



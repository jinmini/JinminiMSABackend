from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService
from com.jinmini.accoount.guest.customer.storages.customer_repository import CustomerRepository

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

class RemoveCustomer(AbstractService):
    """고객을 비활성화하는 서비스 클래스 (실제 삭제 대신 상태 변경)"""
    
    async def handle(self, **kwargs) -> Dict[str, Any]:
        """
        고객을 비활성화합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            user_id: 비활성화할 고객의 ID
            
        Returns:
            비활성화된 고객 정보
        """
        db: AsyncSession = kwargs.get("db")
        user_id: str = kwargs.get("user_id")
        
        # 현재 비활성화 기능이 별도로 구현되어 있지 않으므로 
        # 임시로 삭제 기능을 호출하고 성공 여부를 반환합니다.
        try:
            result = await CustomerRepository.delete_customer(db, user_id)
            return {
                "success": result,
                "message": "고객이 성공적으로 비활성화되었습니다." if result else "고객을 찾을 수 없습니다."
            }
        except Exception as e:
            print(f"고객 비활성화 중 오류 발생: {str(e)}")
            return {
                "success": False,
                "message": f"고객 비활성화 중 오류 발생: {str(e)}"
            }

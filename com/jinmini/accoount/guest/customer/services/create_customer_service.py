from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema
from com.jinmini.accoount.guest.customer.storages.customer_repository import CustomerRepository
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class CreateCustomer(AbstractService):
    """고객 생성 서비스 클래스"""
    
    async def handle(self, **kwargs):
        """
        새로운 고객을 생성하고 데이터베이스에 저장합니다.
        
        Args:
            db: 비동기 데이터베이스 세션
            new_customer: 고객 생성 스키마
            
        Returns:
            생성된 고객 엔티티
        """
        db = kwargs.get("db")
        new_customer = kwargs.get("new_customer")
        
        try:
            # 트랜잭션 시작
            async with db.begin():
                # 고객 생성
                customer = await CustomerRepository.create_customer(db, new_customer)
                
                # 새로 생성된 고객 엔티티 반환
                return customer.to_response()
                
        except Exception as e:
            print(f"고객 생성 중 오류 발생: {str(e)}")
            # 예외 발생 시 롤백은 async with db.begin()에 의해 자동으로 처리됨
            raise e
    



from com.jinmini.utils.creational.abstract.abstract_service import AbstractService
from sqlalchemy.exc import SQLAlchemyError
from com.jinmini.accoount.guest.customer.storages.find_customer import GetAllRepository, GetDetailRepository

# 상수 및 클래스 정의
Get_all = "get_all"
Get_Detail = "get_detail"

class FindCustomer(AbstractService):
    
    async def handle(self, db, **kwargs):
        retrieve_repo = GetAllRepository()
            
        try:
            result = await retrieve_repo.handle(db, **kwargs)
            return result

        except SQLAlchemyError as e:
            print("⚠️ 데이터 조회 중 오류 발생:", str(e))
            return {"error": "데이터 조회 중 오류가 발생했습니다."}

class GetAllCustomer(AbstractService):
    
    async def handle(self, db, **kwargs):
        return await FindCustomer().handle(db, **kwargs)
        
class GetDetailCustomer(AbstractService):
    
    async def handle(self, db, **kwargs):
        # 상세 조회 로직 구현
        detail_repo = GetDetailRepository()
        return await detail_repo.handle(db, **kwargs)






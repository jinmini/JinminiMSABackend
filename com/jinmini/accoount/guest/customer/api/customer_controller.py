from com.jinmini.accoount.guest.customer.api.customer_factory import CustomerFactory
from com.jinmini.accoount.guest.customer.models.customer_action import CustomerAction

class CustomerController:
    
    def __init__(self):
        pass

    async def create_customer(self, **kwargs): # 고객 생성
        return await CustomerFactory.create(strategy=CustomerAction.CREATE_CUSTOMER, **kwargs)

    async def get_customer_by_id(self, **kwargs): # 고객 조회
        return await CustomerFactory.create(strategy=CustomerAction.GET_CUSTOMER_BY_ID, **kwargs)

    async def get_customer_list(self, **kwargs): # 고객 목록 조회
        return await CustomerFactory.create(strategy=CustomerAction.GET_CUSTOMERS, **kwargs)

    async def update_customer(self, **kwargs): # 고객 수정
        return await CustomerFactory.create(strategy=CustomerAction.UPDATE_CUSTOMER, **kwargs)

    async def delete_customer(self, **kwargs): # 고객 삭제
        return await CustomerFactory.create(strategy=CustomerAction.DELETE_CUSTOMER, **kwargs)

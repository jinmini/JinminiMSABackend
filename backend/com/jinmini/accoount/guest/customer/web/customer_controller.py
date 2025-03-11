from com.jinmini.accoount.guest.customer.web.customer_factory import CustomerFactory
from com.jinmini.accoount.guest.customer.strategy.strategy_type import StrategyType

class CustomerController:
    
    def __init__(self):
        pass

    def create_customer(self, **kwargs):
        return CustomerFactory.execute(strategy=StrategyType.DEFAULT_CREATE, method="create", **kwargs)

    def get_customer_detail(self, **kwargs):
        return CustomerFactory.execute(strategy=StrategyType.GET_DETAIL, method="retrieve", **kwargs)
    
    async def get_customer_list(self, db):
        return await CustomerFactory.execute(strategy=StrategyType.GET_ALL, method="retrieve", db=db)

    def update_customer(self, **kwargs):
        return CustomerFactory.execute(strategy=StrategyType.FULL_UPDATE, method="update", **kwargs)
    
    def delete_customer(self, **kwargs):
        return CustomerFactory.execute(strategy=StrategyType.HARD_DELETE, method="delete", **kwargs)
    

    


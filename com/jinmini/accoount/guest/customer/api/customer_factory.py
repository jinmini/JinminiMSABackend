from backend.com.jinmini.accoount.guest.customer.models.customer_action import CustomerAction
from backend.com.jinmini.accoount.guest.customer.services.customer_mutation import CreateCustomer


class CustomerFactory:

    strategy_map = {
        CustomerAction.CREATE_CUSTOMER: CreateCustomer(),
        CustomerAction.GET_CUSTOMER_BY_ID: GetDetailCustomer(),
        CustomerAction.GET_CUSTOMERS: GetAllCustomer(),
        CustomerAction.UPDATE_CUSTOMER: UpdateCustomer(),
        CustomerAction.DELETE_CUSTOMER: DeleteCustomer(),
    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = CustomerFactory.strategy_map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return await instance.handle(**kwargs)


    # @staticmethod
    # async def execute(strategy: CustomerAction, method: Literal["create", "retrieve", 
    #     "update", "delete"], db, **kwargs):

    #     instance = CustomerFactory.strategy_map.get(strategy)
    #     if not instance:
    #         raise ValueError(f"Invalid strategy: {strategy}")
        
    #     if not hasattr(instance, method):
    #         raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")

    #     method_to_call = getattr(instance, method)

    #     if callable(method_to_call):
    #         if method == "retrieve":
    #             return await method_to_call(db=db, **kwargs)  
    #         else:
    #             return method_to_call(db=db, **kwargs)
    #     else:
    #         return TypeError(f"Method '{method}' is not callable.")
   
        
        

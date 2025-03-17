from typing import Literal
from com.jinmini.accoount.guest.customer.models.customer_action import CustomerAction
from com.jinmini.accoount.guest.customer.services.create_customer_service import  CreateCustomer
from com.jinmini.accoount.guest.customer.services.delete_customer_service import DeleteCustomer, RemoveCustomer
from com.jinmini.accoount.guest.customer.services.find_customer_service import  GetAllCustomer, GetDetailCustomer
from com.jinmini.accoount.guest.customer.services.get_customer_service import  UpdateCustomer, PatchCustomer

class CustomerFactory:

    strategy_map = {
        CustomerAction.CREATE_CUSTOMER: CreateCustomer(),
        CustomerAction.FIND_CUSTOMER: GetAllCustomer(),
        CustomerAction.GET_ALL_CUSTOMER: GetAllCustomer(),
        CustomerAction.GET_CUSTOMER_BY_ID: GetDetailCustomer(),
        CustomerAction.UPDATE_CUSTOMER: UpdateCustomer(),
        CustomerAction.PATCH_CUSTOMER: PatchCustomer(),
        CustomerAction.DELETE_CUSTOMER: DeleteCustomer(),
        CustomerAction.REMOVE_CUSTOMER: RemoveCustomer(),
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
   
        
        

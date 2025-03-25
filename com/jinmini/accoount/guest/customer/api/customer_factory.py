from com.jinmini.accoount.guest.customer.services.get_customer_service import GetCustomerById, GetCustomers
from com.jinmini.accoount.guest.customer.services.update_customer_service import UpdateCustomer
from com.jinmini.accoount.guest.customer.services.delete_customer_service import DeleteCustomer
from com.jinmini.accoount.guest.customer.models.customer_action import CustomerAction
from com.jinmini.accoount.guest.customer.services.customer_mutation import CreateCustomer


class CustomerFactory:

    strategy_map = {
        CustomerAction.CREATE_CUSTOMER: CreateCustomer(),
        CustomerAction.GET_CUSTOMER_BY_ID: GetCustomerById(),
        CustomerAction.GET_CUSTOMERS: GetCustomers(),
        CustomerAction.UPDATE_CUSTOMER: UpdateCustomer(),
        CustomerAction.DELETE_CUSTOMER: DeleteCustomer(),
    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = CustomerFactory.strategy_map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return await instance.handle(**kwargs)


   
        
        

import asyncio
from typing import Literal
from com.jinmini.accoount.guest.customer.strategy.strategy_type import StrategyType
from com.jinmini.accoount.guest.customer.strategy.create_strategy import DefaultCreateCustomerStrategy, ValidatedCreateCustomerStrategy
from com.jinmini.accoount.guest.customer.strategy.retrieve_strategy import GetallStrategy, GetDetailStrategy
from com.jinmini.accoount.guest.customer.strategy.update_strategy import FullUpdateCustomerStrategy, PartialUpdateCustomerStrategy
from com.jinmini.accoount.guest.customer.strategy.delete_strategy import SoftDeleteCustomerStrategy, HardDeleteCustomerStrategy

class CustomerFactory:

    strategy_map = {
        StrategyType.DEFAULT_CREATE: DefaultCreateCustomerStrategy(),
        StrategyType.VALIDATED_CREATE: ValidatedCreateCustomerStrategy(),
        StrategyType.GET_DETAIL: GetDetailStrategy(),
        StrategyType.GET_ALL: GetallStrategy(),
        StrategyType.FULL_UPDATE: FullUpdateCustomerStrategy(),
        StrategyType.PARTIAL_UPDATE: PartialUpdateCustomerStrategy(),
        StrategyType.SOFT_DELETE: SoftDeleteCustomerStrategy(),
        StrategyType.HARD_DELETE: HardDeleteCustomerStrategy(),
    }

    @staticmethod
    async def execute(strategy: StrategyType, method: Literal["create", "retrieve", "update", "delete"], **kwargs):
        instance = CustomerFactory.strategy_map[strategy]
        if not instance:
            raise ValueError(f"Invalid strategy: {strategy}")
        
        if not hasattr(instance, method):
            raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")

        method_to_call = getattr(instance, method)

        if asyncio.iscoroutinefunction(method_to_call):
            return await method_to_call(**kwargs)  # 비동기 함수는 await로 호출
        else:
            return method_to_call(**kwargs)
   
        
        

from com.jinmini.accoount.staff.manager.strategy.create_strategy import DefaultCreateManagerStrategy, ValidatedCreateManagerStrategy
from com.jinmini.accoount.staff.manager.strategy.delete_strategy import HardDeleteManagerStrategy, SoftDeleteManagerStrategy
from com.jinmini.accoount.staff.manager.strategy.retrieve_strategy import GetDetailManagerStrategy, GetallManagerStrategy
from com.jinmini.accoount.staff.manager.strategy.strategy_type import StrategyType
from com.jinmini.accoount.staff.manager.strategy.update_strategy import FullUpdateManagerStrategy, PartialUpdateManagerStrategy
import asyncio
from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession

class ManagerFactory:
    
    strategy_map = {
        StrategyType.DEFAULT_CREATE: DefaultCreateManagerStrategy(),
        StrategyType.VALIDATED_CREATE: ValidatedCreateManagerStrategy(),
        StrategyType.GET_DETAIL: GetDetailManagerStrategy(),
        StrategyType.GET_ALL: GetallManagerStrategy(),
        StrategyType.FULL_UPDATE: FullUpdateManagerStrategy(),
        StrategyType.PARTIAL_UPDATE: PartialUpdateManagerStrategy(),
        StrategyType.SOFT_DELETE: SoftDeleteManagerStrategy(),
        StrategyType.HARD_DELETE: HardDeleteManagerStrategy(),
    }

    @staticmethod
    async def execute(strategy: StrategyType, method: Literal["create", "retrieve", "update", "delete"], db: AsyncSession, **kwargs):
        instance = ManagerFactory.strategy_map[strategy]
        if not instance:
            raise ValueError(f"Invalid strategy: {strategy}")
        
        if not hasattr(instance, method):
            raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")
        
        method_to_call = getattr(instance, method)

        if asyncio.iscoroutinefunction(method_to_call):
            return await method_to_call(db=db, **kwargs)
        else:
            return method_to_call(db=db, **kwargs)
        
        



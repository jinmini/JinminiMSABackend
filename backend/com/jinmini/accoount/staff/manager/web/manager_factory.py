
class ManagerFactory:
    
    strategy_map = {
        "create": CreateManagerStrategy(),
        "read_detail": ReadManagerDetailStrategy(),
        "read_list": ReadManagerListStrategy(),
        "update": UpdateManagerStrategy(),
        "delete": DeleteManagerStrategy(),
    }

    @staticmethod
    def create_manager(strategy, **kwargs):
        instance = strategy.map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return instance.handle(**kwargs)

    @staticmethod
    def get_manager_detail(strategy, **kwargs):
        instance = strategy.map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return instance.handle(**kwargs)

    @staticmethod
    def get_manager_list(strategy, **kwargs):
        instance = strategy.map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return instance.handle(**kwargs)

    @staticmethod
    def update_manager(strategy, **kwargs):
        instance = strategy.map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return instance.handle(**kwargs)

    @staticmethod
    def delete_manager(strategy, **kwargs):
        instance = strategy.map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return instance.handle(**kwargs)
        
        




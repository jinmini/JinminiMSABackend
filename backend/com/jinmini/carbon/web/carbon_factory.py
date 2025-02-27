from com.jinmini.carbon.service.carbon_user import CarbonUser

strategy_map = {
    "carbon_user": CarbonUser(),
}

class CarbonFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)

from com.jinmini.carbon.web.carbon_factory import CarbonFactory

class CarbonController:
    
    def __init__(self):
        pass

    def carbon_user(self, **kwargs):
        return CarbonFactory.create(strategy="carbon_user",**kwargs)
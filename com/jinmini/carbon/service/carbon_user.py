
from com.jinmini.carbon.service.abstract_carbon import AbstractCarbon

class CarbonUser(AbstractCarbon):

    def handle(self, **kwargs):
        return "Hello Carbon"
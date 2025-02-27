from abc import ABCMeta, abstractmethod

class AbstractAdmin(metaclass = ABCMeta): 
   
    @abstractmethod
    def handle(self, **kwargs): 
        pass


from abc import ABCMeta, abstractmethod

class AbstractCarbon(metaclass = ABCMeta): 

    @abstractmethod           
    def handle(self, **kwargs): 
        pass
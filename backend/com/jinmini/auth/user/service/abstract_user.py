
from abc import ABCMeta, abstractmethod

class AbstractUser(metaclass = ABCMeta): # 추상 클래스

    @abstractmethod #추상 메소드          
    def handle(self, **kwargs): # handle 메소드
            pass


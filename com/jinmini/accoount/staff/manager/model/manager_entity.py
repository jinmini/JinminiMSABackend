from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from com.jinmini.accoount.common.user.model.user_entity import UserEntity

Base = declarative_base()

class ManagerEntity(UserEntity):

    pass    

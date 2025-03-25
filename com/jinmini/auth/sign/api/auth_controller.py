from com.jinmini.auth.sign.api.auth_factory import AuthFactory
from com.jinmini.auth.sign.models.auth_action import AuthAction

class AuthController:

    def __init__(self):
        pass

    async def signin(self, user_schema, db):
        return await AuthFactory.create(AuthAction.SIGN_IN, user_schema=user_schema, db=db)

    async def signout(self, user_schema, db):
        return await AuthFactory.create(AuthAction.SIGN_OUT, user_schema=user_schema, db=db)
    
    async def signup(self, user_schema, db):
        return await AuthFactory.create(AuthAction.SIGN_UP, user_schema=user_schema, db=db)
    



from com.jinmini.auth.admin.web.admin_factory import AdminFactory

class AdminController:
    
    def __init__(self):
        pass

    def admin_user(self, **kwargs):
        return AdminFactory.create(strategy="admin_user",**kwargs)
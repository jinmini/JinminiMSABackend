from com.jinmini.auth.admin.service.abstract_admin import AbstractAdmin

class AdminUser(AbstractAdmin):

    def handle(self, **kwargs):
        return "Hello Admin"
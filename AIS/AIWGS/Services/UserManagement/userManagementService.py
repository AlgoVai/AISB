from AIWGS.models import Roles,UserRoles,Modules,Menus,RolesPermissions,Permissions

class UserManagementService:

    def createRoles(self,data):
        result = Roles.objects.create(**data)
        return result
    
    def createUserRoles(self,data):
        result = UserRoles.objects.create(**data)
        return result
    
    def createUserModule(self,data):
        result = Modules.objects.create(**data)
        return result
    

    def createUserMenue(self,data):
        result = Menus.objects.create(**data)
        return result
    

    def createUserPermission(self,data):
        result = Permissions.objects.create(**data)
        return result
    
    
    def createUserRolePermission(self,data):
        result = RolesPermissions.objects.create(**data)
        return result


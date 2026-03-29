from drf_yasg.utils import swagger_auto_schema
from rest_framework import status 
from AIWGS.SchemaAnnotor.userManagement.userManagementSchema import postRoleResponse, postRoleSchema ,UserRoleResponse,UserRoleSchema,ModuleSchema,ModulueResponse
def swagger_postRoles(func):
    return swagger_auto_schema(
        tags = ["Roles"],
        request_body = postRoleSchema,
        responses = {status.HTTP_201_CREATED:postRoleResponse}
    )(func)

def swagger_UserRoles(func):
    return swagger_auto_schema(
        tags = ["Roles"],
        request_body = UserRoleSchema,
        responses = {status.HTTP_201_CREATED:UserRoleResponse}
    )(func)

def swagger_UserModule(func):
    return swagger_auto_schema(
        tags = ["Roles"],
        request_body = ModuleSchema,
        responses = {status.HTTP_201_CREATED:ModulueResponse}
    )(func)
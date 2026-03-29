from drf_yasg import openapi
from rest_framework import status

postRoleSchema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties = {
        "Name" : openapi.Schema(type=openapi.TYPE_STRING,default = "Enter your Name"),
        "Description" : openapi.Schema(type=openapi.TYPE_STRING,default = "Enter your description"),
        "IsActive" : openapi.Schema(type=openapi.TYPE_BOOLEAN,default="true")
    },
    required = ["Name","Description","IsActive"]
)
postRoleResponse = openapi.Response(description="Role created successfully !")

UserRoleSchema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties = {
         "userId":openapi.Schema(type=openapi.TYPE_INTEGER,default=1),
          "roleId":openapi.Schema(
              type=openapi.TYPE_ARRAY,
              items=openapi.TYPE_INTEGER,
              example=[1, 2, 3]
          )
    },
    required = ["userId","roleId"]
)
UserRoleResponse = openapi.Response(description="User role created successfully !")



ModuleSchema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties = {
        "Name" : openapi.Schema(type=openapi.TYPE_STRING,default = "Enter your Name"),
        "Code" : openapi.Schema(type=openapi.TYPE_STRING,default="xyz"),
        "Description" : openapi.Schema(type=openapi.TYPE_STRING,default = "Enter your description"),
        
    },
    required = ["Name","Code","Description"]
)
ModulueResponse = openapi.Response(description="Module created successfully !")


MenueSchema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties = {
        "MenueName" : openapi.Schema(type=openapi.TYPE_STRING,default = "Enter Menue Name"),
        "ModuleId" : openapi.Schema(type=openapi.TYPE_INTEGER,default=1),
        "MenuesUrl" : openapi.Schema(type=openapi.TYPE_STRING,default = "Enter menue url"),
        
    },
    required = ["MenueName","ModuleId","MenuesUrl"]
)
MenueResponse = openapi.Response(description="Menue created successfully !")



PermissionSchema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties = {
        "Name" : openapi.Schema(type=openapi.TYPE_STRING,default = "Enter your Name"),
        "CodeName" : openapi.Schema(type=openapi.TYPE_STRING,default="xyz"),
        "moduleId":openapi.Schema(type=openapi.TYPE_INTEGER,default=1),
        "MenuesId" : openapi.Schema(type=openapi.TYPE_INTEGER,default=1),
        "httpMethod" : openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items = openapi.TYPE_STRING,
            example = [2,3,4]
        ),
        "UrlPatter" : openapi.Schema(type=openapi.TYPE_STRING,default = "Enter your description"),
        "IsActive" : openapi.Schema(type=openapi.TYPE_BOOLEAN,default="True"),
        
    },
    required = ["Name","CodeName","moduleId","menuesId","httpMethod","UrlPatter","IsActive"]
)
PermissionResponse = openapi.Response(description="Permission created successfully !")

ModuleSchema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties = {
        "roleId" : openapi.Schema(type=openapi.TYPE_INTEGER,default = 1),
        "PermissionId" : openapi.Schema(type=openapi.TYPE_INTEGER,default=1)
        
    },
    required = ["roleId","PermissionId"]
)
PermissionResponse = openapi.Response(description="Module created successfully !")

from rest_framework import serializers
from AIWGS.models import Roles

class RoleSerializers(serializers.Serializer):
    Name = serializers.CharField()
    Description = serializers.CharField()
    IsActive = serializers.BooleanField()
    def validate_data(self,data):
        if not data:
            return serializers.ValidationError({"Error" : "Data not found !"})
        return data

class UserRoleSerializers(serializers.Serializer):
    userId = serializers.IntegerField()
    roleId = serializers.ListField(
        child = serializers.IntegerField()
    )
    def validate_data(self,data):
        if not data:
            return serializers.ValidationError({"Error" : "Data not found !"})
        return data
    


class ModuleSerializers(serializers.Serializer):
    Name = serializers.CharField()
    Code = serializers.CharField()
    Description = serializers.CharField()
    def validate_data(self,data):
        if not data:
            return serializers.ValidationError({"Error" : "Data not found !"})
        return data
    
class MenuesSerializers(serializers.Serializer):
     MenueName = serializers.CharField(max_length=500)
     ModuleId = serializers.IntegerField()
     MenusUrl = serializers.CharField(max_length=500)
     def validate_data(self,data):
        if not data:
            return serializers.ValidationError({"Error" : "Data not found !"})
        return data


class PermissionsSerializers(serializers.Serializer):
       codeName = serializers.CharField(max_length=200)
       Name = serializers.CharField(max_length=500)
       modeuleId = serializers.IntegerField()
       MenuesId = serializers.IntegerField()
       httpMethod = serializers.ListField(
           child = serializers.CharField()
       )
       urlPatter  = serializers.CharField(null=True)
       IsActive = serializers.BooleanField(default=False)
       def validate_data(self,data):
        if not data:
            return serializers.ValidationError({"Error" : "Data not found !"})
        return data
       

class RolePermissionSerializers(serializers.Serializer):
     roleId = serializers.IntegerField()
     PermissionId = serializers.IntegerField()
     def validate_data(self,data):
        if not data:
            return serializers.ValidationError({"Error" : "Data not found !"})
        return data
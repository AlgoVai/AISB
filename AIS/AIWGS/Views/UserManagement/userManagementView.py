from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from AIWGS.Serializers.userManagement.postUserManagementSerializer import RoleSerializers,UserRoleSerializers,ModuleSerializers
from AIWGS.Services.UserManagement.userManagementService import UserManagementService
from AIWGS.SchemaAnnotor.userManagement.userManagementAnnotor import swagger_postRoles,swagger_UserRoles
from datetime import datetime


class RoleViews(APIView):
    serializers_class = RoleSerializers
    role_service = UserManagementService()
    @swagger_postRoles
    def post(self,request):
        serializer_data = self.serializers_class(data = request.data)
        if serializer_data.is_valid():
            data = serializer_data.validated_data
            res = self.role_service.createRoles(data)
            return Response({"Data Created Successfully"},status = status.HTTP_200_OK)
        return Response("Please create your data again !",status = status.HTTP_400_BAD_REQUEST)
    




class UserRoleViews(APIView):
    serializers_class = UserRoleSerializers
    role_service = UserManagementService()
    @swagger_UserRoles
    def post(self,request):
        serializer_data = self.serializers_class(data = request.data)
        if serializer_data.is_valid():
            data = serializer_data.validated_data
            data["AssignedAt"] = datetime.utcnow()
            res = self.role_service.createUserRoles(data)
            return Response({"Data Created Successfully"},status = status.HTTP_200_OK)
        return Response("Please create your data again !",status = status.HTTP_400_BAD_REQUEST)
    


class UserModuleViews(APIView):
    serializers_class = ModuleSerializers
    role_service = UserManagementService()
    @swagger_UserRoles
    def post(self,request):
        serializer_data = self.serializers_class(data = request.data)
        if serializer_data.is_valid():
            data = serializer_data.validated_data
            res = self.role_service.createUserModules(data)
            return Response({"Module Created Successfully"},status = status.HTTP_200_OK)
        return Response("Please create your module again !",status = status.HTTP_400_BAD_REQUEST)



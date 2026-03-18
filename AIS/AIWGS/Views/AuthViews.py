from rest_framework.views import APIView
from AIWGS.Serializers.AuthSerializer import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from AIWGS.AuthDocs.AuthAnnotor import swagger_login
from AIWGS.Helper.AuthDecoder import AuthDecoder
class LogInAPIVIEW(APIView):

    serializer_class = LoginSerializer

    @swagger_login
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserAPIVIEW(APIView):
    DecoderObject = AuthDecoder();
    def getHeader(self,request):
        auth_header = self.request.GET("Authorization")
        if not auth_header:
            return Response({"error":"Token missing"},status=status.HTTP_401_UNAUTHORIZED)
        token = auth_header.split(" ")[1]
        payload = self.DecoderObject.decode(token)
        if not payload:
            return Response({"error":"Invalid or expired token"},status=status.HTTP_401_UNAUTHORIZED)
        userId = payload.UserId
        InstituteId = payload.InstituteId
        return Response({
            "userId" : userId,
            "InstituteId" : InstituteId
        })
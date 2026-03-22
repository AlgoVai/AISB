from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AIWGS.Serializers.Administration.InstitutionSerializer import InstituteSerializer,InstitutePostSerializer
from AIWGS.Services.Administrations.Institutions import InstituteService
from AIWGS.SchemaAnnotor.AdministrationAnotor import swagger_createInstitution
from datetime import datetime
class InstitionAPIView(APIView):
    serializer_class = InstituteSerializer
    postSerializer_class = InstitutePostSerializer
    inService = InstituteService()

    def get(self,request):
            
            result = self.inService.Get()
            serializer = self.serializer_class(result,many=True)
            return Response(data=serializer.data)
    
    @swagger_createInstitution
    def post(self,request):
          serializer = self.postSerializer_class(data = request.data)

          if serializer.is_valid():
                data = serializer.validated_data
                data['Created_At'] = datetime.utcnow()
                result = self.inService.createInstitute(data)
                return Response({"Institute data created successfully"},status=status.HTTP_200_OK)
         
          return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
          

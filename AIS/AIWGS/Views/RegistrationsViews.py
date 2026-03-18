from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from AIWGS.models import Users
from AIWGS.Serializers.RegistrationSerializers import RegistrationSerializers
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from AIWGS.AuthDocs.AuthAnnotor import swagger_Registration

@swagger_Registration
@api_view(['POST'])
def CreateUser(request):
    serializer = RegistrationSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(
            InstituteId = 1,
            userTypeId = 14,
            BranchId = 1,
            IsActive = True,
        )
        return Response(
            {
  'message':'Data created Successfully',
            'data':serializer.data
            },
              status = status.HTTP_201_CREATED
          
        )
  
    else:
        return Response(
            {
            'message':'Not Created !',
            'errors':serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
         
        )


    

from rest_framework import serializers 
from datetime import datetime , timedelta
from AIS import settings
from AIWGS.models import Users
import jwt
from datetime import timedelta
from AIS.settings import CUSTOM_JWT

class LoginSerializer(serializers.Serializer):
    Email = serializers.EmailField(write_only=True,required = False)
    Password = serializers.CharField(write_only = True,required = False)

    def CreateJwtToken(self,user):
        payload = {
            "userId" : user.userId,
            "InstituteId" : user.InstituteId,
            "exp" : datetime.utcnow() + CUSTOM_JWT["ACCESS_TOKEN_LIFETIME"],
            "ISSUER" : CUSTOM_JWT["ISSUER"] , 
            "AUDIENCE" : CUSTOM_JWT["AUDIENCE"]
        }
        token = jwt.encode(payload=payload,key=CUSTOM_JWT["SIGNING_KEY"],algorithm=CUSTOM_JWT["ALGORITHM"])
        return token

    def validate(self, data):
        Email = data['Email']
        Password = data['Password']

        user = Users.objects.filter(Email = Email , Password = Password).first()
        if user is None:
            return serializers.ValidationError("Your email and password is incorrect")
        
        data['user'] = user
        return data
    
    def to_representation(self, instance):
        user = instance['user']
        token = self.CreateJwtToken(user)
        return {
            "token" :token
        }
    



#18-3-26


    





            

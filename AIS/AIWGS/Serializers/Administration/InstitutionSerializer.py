from rest_framework import serializers

from rest_framework import status
from rest_framework.response import Response
from AIWGS.models import Institute


class InstituteSerializer(serializers.ModelSerializer):
        class Meta:
            model = Institute
            fields = "__all__"

class InstitutePostSerializer(serializers.Serializer):
     Name = serializers.CharField(required=True)
     Url = serializers.ImageField(required = False)
     Address = serializers.CharField(required = True)
     IsActive = serializers.BooleanField(required=True)

     def validate(self, data):
        if not data:
            raise serializers.ValidationError({"detail": "Data Not Found"})
        return data
       
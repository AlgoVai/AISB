from rest_framework import serializers
from AIWGS.models import Users
class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [   'FirstName',
            'LastName',
            'Age',
            'Phone',
            'Password',
            'Email']
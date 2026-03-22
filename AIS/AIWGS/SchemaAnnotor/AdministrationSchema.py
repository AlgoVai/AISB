from drf_yasg import openapi
from rest_framework import status

instituteRequestSchema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "Name" : openapi.Schema(type=openapi.TYPE_STRING,default="Institute Name"),
        "Address" : openapi.Schema(type=openapi.TYPE_STRING,default="Address"),
        "Url" : openapi.Schema(type=openapi.TYPE_STRING,default="https://myimage.come"),
        "IsActive" : openapi.Schema(type=openapi.TYPE_BOOLEAN,default=True)

    },
    required=["Name","Address","IsActive"]
)

InstitutionResponseSchema = openapi.Response(description="Successfully Created")
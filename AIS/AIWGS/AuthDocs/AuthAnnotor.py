from AIWGS.AuthDocs.AuthSchema import LogInResponseSchema , logInRequestSchema ,RegisterResponseSchema,RegRequestSchema
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

def swagger_login(func):
    return swagger_auto_schema(
        tags = ['Users'],
        request_body = logInRequestSchema,
        responses = {status.HTTP_201_CREATED:LogInResponseSchema}

    )(func)

def swagger_Registration(func):
    return swagger_auto_schema(
        method='post',
        tag=['users'],
        request_body = RegRequestSchema, 
        responses= {status.HTTP_201_CREATED:RegisterResponseSchema}
    )(func)
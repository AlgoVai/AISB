from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from AIWGS.SchemaAnnotor.AdministrationSchema import InstitutionResponseSchema,instituteRequestSchema
def swagger_createInstitution(func):
    return swagger_auto_schema(
        tags=["Institutions"],
        request_body=instituteRequestSchema,
        responses= {status.HTTP_201_CREATED:InstitutionResponseSchema}
    )(func)


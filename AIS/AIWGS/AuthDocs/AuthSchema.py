from drf_yasg import openapi
from rest_framework import status

logInRequestSchema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties = {
        "Email":openapi.Schema(type=openapi.TYPE_STRING, default="shoebahmad681@gmail.com"),
        "Password": openapi.Schema(type=openapi.TYPE_STRING, default='9sdfk@S')
    },
    required = ['Email','Password']
)

LogInResponseSchema = openapi.Response(description="LogIn Successful")

RegRequestSchema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
         " FirstName":openapi.Schema(type=openapi.TYPE_STRING,default="shoeb"),
         "LastName" : openapi.Schema(type=openapi.TYPE_STRING,default="Last Name"), 
         "Age" : openapi.Schema(type=openapi.TYPE_INTEGER,default="Age"), 
         "Phone": openapi.Schema(type=openapi.TYPE_STRING,default="Phone"),
         "Password": openapi.Schema(type=openapi.TYPE_STRING,default="Password"),  
         "ConfirmPassword" : openapi.Schema(type=openapi.TYPE_STRING,default="Confirm Password"), 
         "Email" : openapi.Schema(type=openapi.TYPE_STRING,default="Email"), 
    }
)
RegisterResponseSchema = openapi.Response(description="Registration Successfull")
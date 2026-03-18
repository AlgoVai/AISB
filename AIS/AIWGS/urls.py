from django.urls import path
from . import views
from .Views.RegistrationsViews import CreateUser
from .Views.AuthViews import LogInAPIVIEW

urlpatterns = [
path('profile/CreateUser/',CreateUser,name='CreateUser'),
path('Profile/LoginUser/',LogInAPIVIEW.as_view() , name = 'CreateUser')
]
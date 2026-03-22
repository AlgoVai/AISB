from django.urls import path
from . import views
from .Views.RegistrationsViews import CreateUser
from .Views.AuthViews import LogInAPIVIEW
from .Views.Administrations.InstitionView import InstitionAPIView

urlpatterns = [
path('profile/CreateUser/',CreateUser,name='CreateUser'),
path('Profile/LoginUser/',LogInAPIVIEW.as_view() , name = 'CreateUser'),
path("profile/Institute/",InstitionAPIView.as_view(),name="Institutions")
]
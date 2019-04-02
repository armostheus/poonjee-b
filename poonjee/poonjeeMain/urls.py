from django.urls import path
from rest_framework import routers
from .api import UserCredentialsViewset, PoonjeeUsersViewset

from . import views

routerUC = routers.DefaultRouter()
routerUC.register('api/UserCredentials', UserCredentialsViewset, 'poonjeeMain')

routerPU = routers.DefaultRouter()
routerPU.register('api/PoonjeeUsers', PoonjeeUsersViewset, 'poonjeeMain')

urlpatterns = routerUC.urls
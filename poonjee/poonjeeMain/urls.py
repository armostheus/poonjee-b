from django.urls import path
from rest_framework import routers
from .api import UserCredentialsViewset, PoonjeeUsersViewset

from . import views

router = routers.DefaultRouter()
router.register('apiv1/UserCredentials', UserCredentialsViewset, 'poonjeeMain')
router.register('apiv1/PoonjeeUsers', PoonjeeUsersViewset, 'poonjeeMain')

urlpatterns = router.urls
from poonjeeMain.models import User_Credentials, Poonjee_Users
from rest_framework import viewsets,permissions
from .serializers import UserCredentialsSerializer, PoonjeeUsersSerializer

#UserCredentialsViewset
class UserCredentialsViewset(viewsets.ModelViewSet):
    queryset = User_Credentials.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserCredentialsSerializer

#poonjeeUsers Viewsets
class PoonjeeUsersViewset(viewsets.ModelViewSet):
    queryset = Poonjee_Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PoonjeeUsersSerializer
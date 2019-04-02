from rest_framework import serializers
from poonjeeMain.models import User_Credentials, Poonjee_Users


#Poonjee Main Serializer
class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Credentials
        fields = '__all__'

class PoonjeeUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poonjee_Users
        fields = '__all__'
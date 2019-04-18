from rest_framework import serializers
from poonjeeMain.models import User_Credentials, Poonjee_Users, Inventories, Accounts_Info, Product_Location, Product_Shelf_Duration, Products, Purchase_Transactions, Sales_Details, Sales_Transactions, Seller_Info


#Poonjee Main Serializer
class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Credentials
        fields = '__all__'

class PoonjeeUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poonjee_Users
        fields = '__all__'

class InventoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventories 
        fields = '__all__'

class AccountsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts_Info
        fields = '__all__'

class ProductLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Location
        fields = '__all__' 

class ProductShelfDurationSerializer(serializer.ModelSerializer):
    class Meta:
        model = Product_Shelf_Duration
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class PurchaseTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Transactions
        fields = '__all__'

class SalesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales_Details
        fields = '__all__'

class SalesTransactionsSerializer(serializers.ModelSerializer):                       
    class Meta:
        model = Sales_Transactions
        fields = '__all__'

class SellerInfoSerializer(serializers.ModelSerializer):                       
    class Meta:
        model = Seller_Info
        fields = '__all__'
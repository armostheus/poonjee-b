from poonjeeMain.models import User_Credentials, Poonjee_Users, Inventories, Accounts_Info, Product_Location, Product_Shelf_Duration, Products, Purchase_Transactions, Sales_Details, Sales_Transactions, Seller_Info
from rest_framework import viewsets,permissions
from .serializers import UserCredentialsSerializer, PoonjeeUsersSerializer, InventoriesSerializer, AccountsInfoSerializer, ProductLocationSerializer, ProductShelfDurationSerializer, ProductsSerializer, PurchaseTransactionsSerializer, SalesDetailsSerializer, SalesTransactionsSerializer, SellerInfoSerializer

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

class InventoriesViewset(viewsets.ModelViewSet):
    serializer_class = InventoriesSerializer
    queryset = Inventories.objects.all()
    lookup_field = 'id'


class AccountsInfoViewset(viewsets.ModelViewSet):
    serializer_class = AccountsInfoSerializer
    queryset = Accounts_Info.objects.all()
    lookup_field = 'id'

class ProductLocationViewset(viewsets.ModelViewSet):
    serializer_class = ProductLocationSerializer
    queryset = Product_Location.objects.all()
    lookup_field = 'id'

class ProductShelfDurationViewset(viewsets.ModelViewSet):
    serializer_class = ProductShelfDurationSerializer
    queryset = Product_Shelf_Duration.objects.all()
    lookup_field = 'id'

class ProductsViewset(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    lookup_field = 'id'

class PurchaseTransactionsViewset(viewsets.ModelViewSet):
    serializer_class = PurchaseTransactionsSerializer
    queryset = Purchase_Transactions.objects.all()
    lookup_field = 'transaction_id'

class SalesDetailsViewset(viewsets.ModelViewSet):
    serializer_class = SalesDetailsSerializer
    queryset = Sales_Details.objects.all()
    lookup_field = 'transaction_id'


class SalesTransactionsViewset(viewsets.ModelViewSet):
    serializer_class = SalesTransactionsSerializer
    queryset = Sales_Transactions.objects.all()
    lookup_field = 'transaction_id'

class SellerInfoViewset(viewsets.ModelViewSet):
    serializer_class = SellerInfoSerializer
    queryset = Seller_Info.objects.all()
    lookup_field = 'id'
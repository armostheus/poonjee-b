from django.urls import path
from rest_framework import routers
from .api import UserCredentialsViewset, PoonjeeUsersViewset

from . import views

router = routers.DefaultRouter()
router.register('apiv1/UserCredentials', UserCredentialsViewset, 'poonjeeMain')
router.register('apiv1/PoonjeeUsers', PoonjeeUsersViewset, 'poonjeeMain')
router.register('apiv1/AccountsInfo', AccountsInfoViewset)
router.register('apiv1/ProductLocation', ProductLocationViewset)
router.register('apiv1/ProductShelfDuration', ProductShelfDurationViewset)
router.register('apiv1/Products', ProductsViewset)
router.register('apiv1/PurchaseTransactions', PurchaseTransactionsViewset)
router.register('apiv1/SalesDetails', SalesDetailsViewset)
router.register('apiv1/SalesTransactions', SalesTransactionsViewset)
router.register('apiv1/SellerInfo', SellerInfoViewset)

urlpatterns = router.urls
from django.urls import path
from . import views

from store.view_classes.store import *
from store.view_classes.cart import *
from store.view_classes.checkout import *
from store.view_classes.ajax import *
from store.view_classes.account import *

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('cart/', CartView.as_view(), name='cart'),
    path('update_cart/', UpdateCart.as_view(), name='update_cart'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('checkout/<str:action>/', CheckOutView.as_view(),
         name='checkout_with_action'),
    path('account/address/', AddressView.as_view(), name='account_address'),
    path('account/address/<int:id>/',
         AddressView.as_view(), name='account_address_by_id'),
]

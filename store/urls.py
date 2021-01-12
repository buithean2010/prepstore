from django.urls import path
from . import views

from store.view_classes.store import *
from store.view_classes.cart import *
from store.view_classes.ajax import *

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('cart/', CartView.as_view(), name='cart'),
    path('update_cart/', UpdateCart.as_view(), name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
]

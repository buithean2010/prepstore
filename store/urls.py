from django.urls import path
from . import views

from store.view_classes.store import *

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]

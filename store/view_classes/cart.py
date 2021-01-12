from .base import BaseView, TitleConst
from django.shortcuts import render

from ..data_access_objects.cartDAO import *


class CartView(BaseView):
    '''
    Cart's View
    '''

    def __init__(self):
        super().__init__("store/cart.html")

    def set_context(self):
        is_mobile_device = False
        if "mobile" in self.request.META['HTTP_USER_AGENT'].lower():
            is_mobile_device = True

        r = self.request
        if r.user.is_authenticated:
            customer = r.user.customer
            order, created = Orders.objects.get_or_create(
                customer=customer, complete_flg=False)
            items = order.orderitems_set.all()
        else:
            items = []

        context = {
            'title': TitleConst.CART_VIEW_TITLE,
            'cart': {},
            'order': order,
            'items': items,
            'image_base': self.get_image_base(),
            'is_mobile_device': is_mobile_device,
        }

        return context

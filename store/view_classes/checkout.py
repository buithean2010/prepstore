from django.shortcuts import render
from .base import BaseView, TitleConst

from ..form import ShippingAddressForm
from ..models import ShippingAddress, Orders


class CheckOutView(BaseView):
    '''
    CheckOut's View
    '''

    def __init__(self):
        super().__init__("store/checkout.html")

    def set_context(self):
        form = ShippingAddressForm(self.request.POST or None)
        shipping_addr = None
        shipping_addresses = []

        if self.request.user.is_authenticated:
            # login user
            # get default shipping address
            shipping_addr = ShippingAddress.objects.filter(
                customer=self.customer).first()
            shipping_addresses = ShippingAddress.objects.filter(
                customer=self.customer)
            # get cart items
            order, created = Orders.objects.get_or_create(
                customer=self.customer, complete_flg=False)
            items = order.orderitems_set.all()
        else:
            # not login user
            items = []

        context = {
            'title': TitleConst.CHECK_OUT_TITLE,
            'form': form,
            'order': order,
            'shipping_addr': shipping_addr,
            'shipping_addresses': shipping_addresses,
            'items': items,
        }

        return context

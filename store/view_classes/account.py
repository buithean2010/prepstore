from django.shortcuts import render
from .base import BaseView, TitleConst
from ..models import *
from ..form import ShippingAddressForm


class AddressView(BaseView):
    '''
    Address's View
    '''

    def __init__(self):
        super().__init__("store/account_address.html")

    def set_context(self):
        # Set defaul values
        addresses = []
        has_address = False
        address_id = None

        # Default value for address form
        form = ShippingAddressForm(self.request.POST or None)

        r = self.request
        if r.user.is_authenticated:
            # Get address list
            customer = r.user.customer
            addresses = ShippingAddress.objects.filter(customer=customer)
            has_address = addresses.count() > 0

            address_id = self.kwargs.get('id')
            action = ''

            if self.request.GET.get('action'):
                action = 'add'

            if address_id:
                # Case: Edit address
                # Get address for customer by id
                addr = ShippingAddress.objects.get(
                    pk=address_id, customer=customer)
                if addr:
                    form = ShippingAddressForm(addr)
                    action = 'edit'

        context = {
            'title': TitleConst.ACCOUNT_ADDRESS_TITLE,
            'form': form,
            'has_address': has_address,
            'addresses': addresses,
            'action': action,
        }

        return context

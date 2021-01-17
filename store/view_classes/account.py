from django.shortcuts import redirect
from .base import BaseView, TitleConst
from ..models import *
from ..form import ShippingAddressForm


class AddressView(BaseView):
    '''
    Address's View
    '''
    # region INIT

    def __init__(self):
        super().__init__("store/account_address.html")

    # endregion

    # region GET
    def set_context(self):
        # Set defaul values
        addresses = []
        has_address = False
        address_id = None

        # Default value for address form
        form = ShippingAddressForm(instance=ShippingAddress())

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
                    form = ShippingAddressForm(instance=addr)
                    action = 'edit'

        context = {
            'title': TitleConst.ACCOUNT_ADDRESS_TITLE,
            'form': form,
            'has_address': has_address,
            'addresses': addresses,
            'action': action,
            'address_id': address_id,
        }

        return context
    # endregion

    # region POST
    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)

    #     # Set Form
    #     self.context['form'] = ShippingAddressForm(self.request.POST)

    #     pass

    def set_form(self):
        return ShippingAddressForm(self.request.POST)

    def set_post_context(self):
        customer = self.request.user.customer
        addresses = ShippingAddress.objects.filter(customer=customer)
        has_address = addresses.count() > 0

        form = self.context['form']
        action = 'add'
        if form.data.get('id'):
            action = 'edit'
        context = {
            'title': TitleConst.ACCOUNT_ADDRESS_TITLE,
            'has_address': has_address,
            'addresses': addresses,
            'action': action,
            'address_id': form.data.get('id'),
        }
        return context

    def process_valid_form(self):
        if self.request.user.is_authenticated:
            # Login user
            try:
                pk = int(self.request.POST.get('id'))
            except:
                pk = None
            customer = self.request.user.customer

            if pk:
                # Edit
                instance = ShippingAddress.objects.get(
                    pk=pk, customer=customer)
            else:
                # Add
                instance = ShippingAddress()

            form1 = ShippingAddressForm(
                self.request.POST, instance=instance)
            model_instance = form1.save(commit=False)
            # Add customer back to model
            model_instance.customer = customer
            model_instance.save()

        else:
            # Anonymous user
            pass
        return redirect('account_address')

    # endregion

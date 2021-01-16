from django.shortcuts import redirect

from .form import ShippingAddressForm


def update_address(request):
    if request.POST:
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            # update or save data
            pass
        else:
            return redirect()

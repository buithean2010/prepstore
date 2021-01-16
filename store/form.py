from django.forms import ModelForm
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = "__all__"
        # fields = ['first_name', 'last_name', 'company_name', 'country',
        #           'region', 'post_no', 'address_1', 'address_2', 'address_3', 'phone_no', 'default_flg']

    def clean(self):
        data = self.cleaned_data
        aa = 1

from django.forms import ModelForm
from .models import ShippingAddress, Regions

import re


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = "__all__"
        # fields = ['first_name', 'last_name', 'company_name', 'country',
        #           'region', 'post_no', 'address_1', 'address_2', 'address_3', 'phone_no', 'default_flg']

    def clean(self):
        data = self.cleaned_data

        name_pattern = re.compile("^([A-Za-z]+)+$")
        company_pattern = re.compile("^([A-Za-z0-9.,\-]+)+$")
        address_pattern = re.compile("^([A-Za-z0-9.,\-]+)+$")
        phone_pattern = re.compile("^([0-9\+\-]+)+$")

        # Validate first_name
        val = data.get('first_name')
        if not val or not name_pattern.match(val):
            self.add_error('first_name', '英字で入力してください。')

        # Validate last_name
        val = data.get('last_name')
        if not val or not name_pattern.match(val):
            self.add_error('last_name', '英字で入力してください。')

        # Validate company_name
        val = data.get('company_name')
        if val:
            if not company_pattern.match(val.replace(' ', '')):
                self.add_error(
                    'company_name', '英数字、コンマ(,)、ドット(.)、ハイフン(-)、半角スペースのみで入力してください。')

        # Validate region
        val = data.get('region')
        try:
            region = Regions.objects.get(romaji_name=val)
            if region is None:
                self.add_error('region', '都道府県を選択してください。')
        except:
            self.add_error('region', '都道府県を選択してください。')

        # Validate post_no
        val = data.get('post_no')
        if not val or not val.isnumeric():
            self.add_error('post_no', '郵便番号を数字で入力してください。')

        # Validate address_1
        val = data.get('address_1')
        if not val or not company_pattern.match(val.replace(' ', '')):
            self.add_error(
                'address_1', '英数字、コンマ(,)、ドット(.)、ハイフン(-)、半角スペースのみで入力してください。')

        # Validate address_2
        val = data.get('address_2')
        if val:
            if not company_pattern.match(val.replace(' ', '')):
                self.add_error(
                    'address_3', '英数字、コンマ(,)、ドット(.)、ハイフン(-)、半角スペースのみで入力してください。')

        # Validate phone_no
        val = data.get('phone_no')
        if not val or not phone_pattern.match(val):
            self.add_error(
                'phone_no', '英数字、コンマ(,)、ドット(.)、ハイフン(-)、半角スペースのみで入力してください。')

        return data

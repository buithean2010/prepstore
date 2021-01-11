from django.shortcuts import render
from .base import BaseView


from ..data_access_objects.storeDAO import *


class StoreView(BaseView):
    '''
    Display Symptoms for each body part
    '''

    def __init__(self):
        super().__init__("store/store.html")

    def set_context(self):
        products = get_all_products()

        context = {
            'title': 'PREP購入代行サービス',
            'products': products,
            'image_base': self.get_image_base(),
        }

        return context

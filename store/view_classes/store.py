from django.shortcuts import render
from .base import BaseView, TitleConst


from ..data_access_objects.storeDAO import *


class StoreView(BaseView):
    '''
    Store's View
    '''

    def __init__(self):
        super().__init__("store/store.html")

    def set_context(self):
        products = get_all_products()

        context = {
            'title': TitleConst.STORE_VIEW_TITLE,
            'products': products,
            'image_base': self.get_image_base(),
        }

        return context

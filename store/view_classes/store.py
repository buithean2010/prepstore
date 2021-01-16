from django.shortcuts import render
from .base import BaseView, TitleConst

from ..models import Products


class StoreView(BaseView):
    '''
    Store's View
    '''

    def __init__(self):
        super().__init__("store/store.html")

    def set_context(self):
        products = Products.objects.all()

        context = {
            'title': TitleConst.STORE_VIEW_TITLE,
            'products': products,
        }

        return context

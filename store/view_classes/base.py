from django.shortcuts import render
from django.views import View
from django.conf import settings
import datetime

from ..models import Orders


class BaseView(View):
    def __init__(self, tpl_name):
        self.template_name = tpl_name
        self.context = {}
        self.request_params = {}
        self.customer = None

    def get(self, request, *args, **kwargs):
        self.request_params = kwargs
        self.context = self.get_cart_info(request.user)
        self.context.update(self.set_context())

        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        pass

    def set_context(self):
        pass

    def get_image_base(self):
        host = ''
        if settings.DEBUG:
            host = 'http://127.0.0.1:8000/'

        return host

    def set_cookie(self, response, key, value, days_expire=7):
        if days_expire is None:
            max_age = 365 * 24 * 60 * 60  # one year
        else:
            max_age = days_expire * 24 * 60 * 60
        expires = datetime.datetime.strftime(
            datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
            "%a, %d-%b-%Y %H:%M:%S GMT",
        )
        response.set_cookie(
            key,
            value,
            max_age=max_age,
            expires=expires,
            domain=settings.SESSION_COOKIE_DOMAIN,
            secure=settings.SESSION_COOKIE_SECURE or None,
        )

    def get_cart_info(self, usr):
        if usr.is_authenticated:
            self.customer = usr.customer

            order, created = Orders.objects.get_or_create(
                customer=self.customer, complete_flg=False)

            cartItems = order.count_cart_items
        else:
            cartItems = 0

        return {'cartItems': cartItems}


class TitleConst:
    STORE_VIEW_TITLE = 'PREP購入代行サービス'
    CART_VIEW_TITLE = 'PREP購入代行サービス'

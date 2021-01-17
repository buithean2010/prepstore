from django.shortcuts import render
from django.views import View
from django.conf import settings
import datetime

from ..models import Orders


class BaseView(View):
    # region INIT
    def __init__(self, tpl_name):
        """
        Init
        """
        self.template_name = tpl_name
        self.context = {}
        self.customer = None

    # endregion

    # region GET
    def get(self, request, *args, **kwargs):
        """
        GET Method
        """
        self.context = self.get_cart_info(request.user)
        self.context.update({'image_base': self.get_image_base()})
        child_context = self.set_context()
        if child_context:
            self.context.update(child_context)

        return render(request, self.template_name, self.context)

    def set_context(self):
        pass

    # endregion

    # region POST
    def post(self, request, *args, **kwargs):
        """
        POST Method
        """
        form = self.set_form()
        if form.is_valid():
            return self.process_valid_form()
        else:
            self.context = self.get_cart_info(request.user)
            self.context.update({'image_base': self.get_image_base()})
            self.context.update({'form': form})
            child_context = self.set_post_context()
            if child_context:
                self.context.update(child_context)
            return render(request, self.template_name, self.context)

    def set_form(self):
        pass

    def set_post_context(self):
        pass

    def process_valid_form(self):
        pass

    # endregion

    # region UTILS
    def get_image_base(self):
        host = HostUrl.HOST_URL
        if settings.DEBUG:
            host = HostUrl.DEBUG_URL

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

    # endregion


class TitleConst:
    STORE_VIEW_TITLE = 'PREP購入代行サービス'
    CART_VIEW_TITLE = 'PREP購入代行サービス'
    CHECK_OUT_TITLE = 'PREP購入代行サービス'
    ACCOUNT_ADDRESS_TITLE = 'PREP購入代行サービス'


class HostUrl:
    DEBUG_URL = 'http://127.0.0.1:8000/'
    HOST_URL = ''

from django.shortcuts import render
from django.views import View
from django.conf import settings


class BaseView(View):
    def __init__(self, tpl_name):
        self.template_name = tpl_name
        self.context = {}
        self.request_params = {}

    def get(self, request, *args, **kwargs):
        self.request_params = kwargs
        self.context = self.set_context()
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

from django.views import View
from django.http import JsonResponse
import json

from ..models import *


class UpdateCart(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        cust = request.user.customer
        product = Products.objects.get(id=productId)

        order, created = Orders.objects.get_or_create(
            customer=cust, complete_flg=False)

        orderItem, created = OrderItems.objects.get_or_create(
            order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse('Item was added', safe=False)

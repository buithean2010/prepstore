from ..models import *


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitems_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}

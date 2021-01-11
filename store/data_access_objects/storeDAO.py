from ..models import Products


def get_all_products():
    return Products.objects.all()

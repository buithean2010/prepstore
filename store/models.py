from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    price = models.IntegerField()
    img_url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete_flg = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItems(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Orders, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Orders, on_delete=models.SET_NULL, null=True, blank=True)
    post_no_1 = models.CharField(max_length=3)
    post_no_2 = models.CharField(max_length=4)
    address_1 = models.CharField(max_length=512)
    address_1_kana = models.CharField(max_length=512)
    address_2 = models.CharField(max_length=512)
    address_2_kana = models.CharField(max_length=512)
    address_3 = models.CharField(max_length=512, null=True, blank=True)
    address_3_kana = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f'〒{post_no_1}-{post_no_2}{address_1}{address_2}{address_3}'

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.
from .const import *


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=512, null=True, blank=True)
    points = models.IntegerField(default=0)
    introducer = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)

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
    complete_date = models.DateTimeField(blank=True, null=True)
    complete_flg = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.IntegerField(default=0)
    tracking_no = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def count_cart_items(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_status(self):
        return OrderStatus.ORDER_STATUS_CHOICES[self.status]


class OrderItems(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Orders, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


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


class PointLog(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    log_type = models.IntegerField()  # 1:還元 2:友達紹介 3:友達購入還元 9:消費
    change_type = models.IntegerField()  # 1:add 2:minus
    log_date = models.DateTimeField(default=datetime.now)

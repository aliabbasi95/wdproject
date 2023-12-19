from django.contrib.auth.models import User
from django.db import models

from product.models import Book


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class BookCountCart(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    count=models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(ShoppingCart,on_delete=models.CASCADE)


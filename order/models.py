from django.contrib.auth.models import User
from django.db import models

from product.models import Book


class ShoppingOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    finalize = models.BooleanField(default=False)

    @property
    def total_price(self):
        sum_price = 0
        for book_count in self.order_book_count.all():
            sum_price += book_count.count * book_count.book.price
        return sum_price


class BookCountOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(ShoppingOrder, on_delete=models.CASCADE, related_name='order_book_count')

from django.contrib import admin

from order.models import ShoppingOrder, BookCountOrder


@admin.register(ShoppingOrder)
class ShoppingOrderAdmin(admin.ModelAdmin):
    pass

@admin.register(BookCountOrder)
class BookCountOrderAdmin(admin.ModelAdmin):
    pass

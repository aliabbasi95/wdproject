from django.urls import path
from cart.views import add_to_cart, shopping_cart_view, remove_book

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('shopping-cart/', shopping_cart_view, name='shopping_cart'),
    path('remove-book/', remove_book, name='remove_book'),

]

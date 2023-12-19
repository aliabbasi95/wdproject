from django.urls import path
from order.views import order_view, finalize_order_view

urlpatterns = [
    path('order/', order_view, name='order'),
    path('finalize-order/', finalize_order_view, name='finalize_order'),

]

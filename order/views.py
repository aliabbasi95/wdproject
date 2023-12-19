from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from order.models import BookCountOrder, ShoppingOrder


@login_required
def order_view(request):
    orders = ShoppingOrder.objects.filter(user=request.user,finalize=False)


    context = {
        'orders':orders
    }
    return render(request, 'order/order.html', context)


def finalize_order_view(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = get_object_or_404(ShoppingOrder, pk=order_id)
        order.finalize=True
        order.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
from django.shortcuts import render

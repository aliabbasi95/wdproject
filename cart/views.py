from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from cart.models import ShoppingCart, BookCountCart
from product.models import Book


@login_required
def shopping_cart_view(request):
    user_shopping_cart = ShoppingCart.objects.get(user=request.user)

    books_in_cart = BookCountCart.objects.filter(cart=user_shopping_cart)

    context = {
        'books_in_cart': books_in_cart
    }
    return render(request, 'cart/shopping_cart.html', context)


def add_to_cart(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)

        shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)
        book_count_cart, created = BookCountCart.objects.get_or_create(cart=shopping_cart, book=book)
        if not created:
            book_count_cart.count = book_count_cart.count + 1
        book_count_cart.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def remove_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        shopping_cart = get_object_or_404(ShoppingCart, user=request.user)
        book_count_cart = get_object_or_404(BookCountCart, cart=shopping_cart, book=book)
        if book_count_cart.count < 2:
            book_count_cart.delete()
        else:
            book_count_cart.count = book_count_cart.count - 1
            book_count_cart.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

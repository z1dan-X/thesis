from django.shortcuts import render
from .models import CartItem, Checkout, CheckoutProducts
from .forms import CheckoutForm


def show_shopping_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(int(cart_item.product.price) * cart_item.quantity for cart_item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)


def show_checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(int(cart_item.product.price) * cart_item.quantity for cart_item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkout = Checkout.objects.create(
                user=request.user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                total_price=total_price,
            )
            for cart_item in cart_items:
                CheckoutProducts.objects.create(
                    checkout=checkout,
                    product=cart_item.product,
                    price=cart_item.product.price,
                    quantity=cart_item.quantity
                )
            cart_items.delete()
            return render(request, 'success_order.html')
    else:
        form = CheckoutForm()

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form
    }
    return render(request, 'checkout.html', context)
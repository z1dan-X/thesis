from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from apps.shop.models import Category, Product, Comment
from apps.shop.forms import CommentForm
from apps.checkout.models import CartItem


def show_shop_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(slug__icontains=query)
        )

    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'shop.html', context)


def show_product_detail_page(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data.get('text')

            Comment.objects.create(
                product=product,
                user=request.user,
                text=user_text
            )
            return redirect('shop:product_detail', slug=product.slug)
    else:
        form = CommentForm()

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'product_detail.html', context)


def add_or_delete_wishlist(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    if product in request.user.wishlist.product.all():
        request.user.wishlist.product.remove(product)
    else:
        request.user.wishlist.product.add(product)
    return redirect('users:wishlist')


def add_product_to_cart(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('checkout:cart_detail')


def delete_product_from_cart(request, product_slug):
    product = CartItem.objects.filter(user=request.user, product__slug=product_slug).first()
    if product.quantity == 0:
        product.delete()
        return redirect('checkout:cart_detail')
    elif product.quantity > 0:
        product.quantity -= 1
        product.save()
        return redirect('checkout:cart_detail')
    else:
        return redirect('checkout:cart_detail')

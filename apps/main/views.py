from django.shortcuts import render
from django.core.paginator import Paginator
from apps.main.models import Discount
from apps.shop.models import Product, Category


def show_home_page(request):
    discount = Discount.objects.all().order_by('-created_at').first()
    products = Product.objects.all()
    categories = Category.objects.order_by('-created_at')[:3]

    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'discount': discount,
        'products': products,
        'categories': categories,
    }

    return render(request, 'index.html', context)


def show_about_us_page(request):
    return render(request, 'about-us.html')

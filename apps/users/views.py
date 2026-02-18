from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import Wishlist


def Registration_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save()
            Wishlist.objects.get_or_create(user=new_user)
            return redirect('users:login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'registration_form.html', context)


def Login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:home')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'login_form.html', context)


def Logout_page(request):
    logout(request)
    return redirect('main:home')


def show_wishlist_page(request):
    wishlist = Wishlist.objects.filter(user=request.user).first()

    products = wishlist.product.all()
    context = {
        'products': products
    }
    return render(request, 'wishlist.html', context)
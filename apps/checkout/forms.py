from django import forms
from apps.checkout.models import Checkout


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['first_name', 'last_name', 'email', 'phone_number']

        first_name = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your first name'
            }),
            label=''
        )
        last_name = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your last name'
            }),
            label=''
        )
        email = forms.EmailField(
            widget=forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'e.g Saymon@gmail.com'
            }),
            label=''
        )
        phone_number = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'e.g. +998 99 123-45-67'
            }),
            label=''
        )
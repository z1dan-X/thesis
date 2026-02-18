from django import forms
from apps.shop.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4',
                'style': 'resize: none; width:100%;',
                'placeholder': 'Напишите свое мнение о товаре'
            }),
        }

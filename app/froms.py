from django import forms
from .models import Item,Login

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['image','product','description', 'price']

class loginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'password': forms.PasswordInput
                (attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
        }

        
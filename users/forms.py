from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,
    widget = forms.EmailInput(attrs={'class' : 'form-control', 'placeholder':'Yourid@gmail.com'})
    )
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label })
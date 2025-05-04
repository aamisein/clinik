from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            'id': 'username',
            'class': 'w-full px-4 py-2 pl-10 mt-1 border rounded-lg focus:ring-2 focus:ring-indigo-400 focus:outline-none',
            'placeholder': 'ایمیل خود را وارد کنید'
        }),
        required=True,
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'class': 'w-full px-4 py-2 pl-10 mt-1 border rounded-lg focus:ring-2 focus:ring-indigo-400 focus:outline-neutral-950',
            'placeholder': 'رمز عبور خود را وارد کنید'
        }),
        required=True,
    )

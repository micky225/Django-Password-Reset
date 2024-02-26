from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class':'form-control',
                'required':True,
                'placeholder': 'Email Address'
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "required": True,
                "placeholder": "Password",
                "minlength": "8"
            }
        ),
    )
    password_confirm = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "required": True,
                "placeholder": "Re-enter password",
                "minlength": "8"
            }
        ),
    )



class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "required": True,
                "placeholder": "Email Address",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "required": True,
                "placeholder": "Password",
            }
        ),
    )


class VerifyEmailForm(forms.Form):
    code = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "required": True,
                "placeholder": "Enter Code",
            }
        ),
    )

class RequestPasswordResetForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "required": True,
                "placeholder": "Enter email",
            }
        ),
    )

class PasswordResetForm(forms.Form):
    code = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "required": True,
                "placeholder": "Enter Code",
            }
        ),
    )
    new_password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "required": True,
                "placeholder": "Enter password",
                "minlength": "8"
            }
        ),
    )
    new_password_confirm = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "required": True,
                "placeholder": "Re-enter password",
                "minlength": "8"
            }
        ),
    )
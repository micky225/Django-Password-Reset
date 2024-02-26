from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import (
    RegistrationForm, 
    LoginForm, VerifyEmailForm, 
    RequestPasswordResetForm,
    PasswordResetForm
)
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import UserEmailVerification
from django.contrib.auth import authenticate, login, logout
from .utils import send_raw_email
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

def home(request):
    return render(request, 'index.html')



def register_view(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_confirm']:
                messages.error(request, "Password fields do not match")
            else:
                user = User.objects.create_user(
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
                )
                code = UserEmailVerification.objects.create(user=user)
                send_raw_email(
                    subject="User Accounts Verification",
                    sender="mickytod03@gmail.com",
                    recipients=[user.email],
                    message=f"""
Hi {user.email},

We just need to verify your email address before you can access our site.

Use the code below to verify your email address

CODE : {code.code}

Thanks!
    """)
                return redirect(
                    reverse('user_account:verify_email', kwargs={'email': user.email})
                )
        else:
            messages.error(request, form.errors)
    context = {
        "form": form
	}
    return render(request, "register.html", context)




def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                is_verified = UserEmailVerification.objects.filter(
                    user=user,
                    is_verified=True
                ).exists()
                if not is_verified:
                    return redirect(
                        reverse('user_account:verify_email', kwargs= {'email':user_email})
                    )
                login(request, user)
                return redirect('user_account:home')    
            else:
                messages.error(request, form.errors)
        else:
            messages.error(request, form.errors)  

    context = {
        'form': form
    }              
    return render(request, "login.html", context)   



def logout_view(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect ("user_account:login")

def request_password_reset_view(request):
    form = RequestPasswordResetForm()
    if request.method == "POST":
        form = RequestPasswordResetForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data["email"])
                try:
                    UserEmailVerification.objects.get(user=user).delete()
                except: ...
                code = UserEmailVerification.objects.create(user=user)
                send_raw_email(
                subject="User Accounts Verification",
                    sender="mickytod03@gmail.com",
                    recipients=[user.email],
                    message=f"""
Hi {user.email},

Use the code below to reset your password

CODE : {code.code}

Thanks! 
    """)
                return redirect(
                    reverse('user_account:reset_password', kwargs={'email': user.email})
                )
            except:
                messages.error(request, 'User with this email does not exist')
        else:
            messages.error(request, form.errors)
    context = {
        "form":form
    }

    return render(request, "request_password_reset.html", context)   


def verify_email_view(request, email):
    form = VerifyEmailForm()
    if request.method == "POST":
        form = VerifyEmailForm(request.POST)
        if form.is_valid():
            try:
                user_code = UserEmailVerification.objects.get(
                    user__email=email,
                    code = form.cleaned_data['code']
                )
                user_code.is_verified = True
                user_code.save()
                user = User.objects.get(email=email)
                login(request, user)
                messages.success(request, "Login successful")
                return redirect('user_account:home',)
            except:
                messages.error(request, "Verification failed! Please check your mail to provide a correct code")
        else:
            messages.error(request, form.errors)
    context = {
        "form": form,
        "email": email
	}
    return render(request, 'verify_email.html', context)


def reset_password(request, email):
    form = PasswordResetForm()
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['new_password'] != form.cleaned_data["new_password_confirm"]:
                messages.error(request, "Passwords do not match")
            elif not UserEmailVerification.objects.filter(user__email=email, code=form.cleaned_data["code"]).exists():
                messages.error(request, "Password reset failed, code provided is invalid")
            else:
                user = User.objects.get(email=email)
                user.set_password(form.cleaned_data["new_password"])
                UserEmailVerification.objects.filter(user__email=email, code=form.cleaned_data["code"]).update(is_verified=True)
                user.save()
                messages.success(request, 'Password reset successful')
                return redirect('user_account:login')
        else:
            messages.error(request, form.errors)
    context = {
        "form":form
    }
    return render(request, 'reset_password.html', context)    
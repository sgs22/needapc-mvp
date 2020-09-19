from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import (
    LoginForm,
    RegisterForm
)
# Create your views here.
def logout_view(request):
    # form 
    logout(request)
    return redirect("/login")

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # verify valid username and password
        user = authenticate(username=username, password=password)
        if user == None:
            print("user is invalid")
            # later add message
            return redirect("/login")
        # perform login
        login(request, user)

        # redirect to a logged in required page
        return redirect("/")

    return render(request, "accounts/login.html", {"form":form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user_obj.is_active = False
        user_obj.save()
        user_obj.set_password(password)
        user_obj.save()
        # send email confirmation
        return redirect("/login")
    return render(request, "accounts/register.html", {"form": form})

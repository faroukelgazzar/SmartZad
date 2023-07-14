from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from .forms import SignUpForm, UserForm

#from systemusers.forms import UserForm, UserProfileInfoForm
import django.contrib.auth.hashers as hasher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    User = request.user
    if User.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'accounts/login.html', {})



def user_login(request):
    if request.method == "POST":
        email   = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Acount is not")

        else:
            print("someone is trying to login")
            return render(request, 'accounts/login.html', {})

    else:
        return render(request, 'accounts/login.html', {})


@login_required
def special(request):
    return HttpResponse("You Are logged in")


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'accounts/login.html', {})




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})




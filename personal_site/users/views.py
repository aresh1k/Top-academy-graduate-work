from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def user_account(request):
    return render(request, 'users/account.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Username does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, 'users/login.html')


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('main')

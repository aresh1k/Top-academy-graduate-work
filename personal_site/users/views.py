from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm, LoginForm


def user_account(request, pk):
    account_data = Profile.objects.get(id=pk)
    context = {
        'account': account_data,
    }
    return render(request, 'users/account.html', context)


def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Учетная запись успешно создана!')
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Произошла непредвиденная ошибка во время регистрации")

    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/registration.html', context)


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
            messages.error(request, 'Username or password is incorrect')

    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def user_logout(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('main')

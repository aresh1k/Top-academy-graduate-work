from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm, LoginForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required


def user_profile(request, pk):
    account_data = Profile.objects.get(id=pk)
    context = {
        'account': account_data,
    }
    return render(request, 'users/account.html', context)


def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Учетная запись успешно создана!')
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Произошла непредвиденная ошибка во время регистрации")
            return redirect('registration')

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
            messages.error(request, 'Такое имя пользователя не существует')
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Вы успешно зашли под учетной записью!')
            return redirect('main')
        else:
            messages.error(request, 'Введен неверный пароль')
            return redirect('login')

    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли из учетной записи!')
    return redirect('main')


@login_required
def user_profile_settings(request):
    profile_data = Profile.objects.get(id=request.user.id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile_data)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль обновлен!')
            return redirect('account', request.user.id)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=profile_data)

    return render(request, 'users/account_settings.html', {'user_settings_form': user_form, 'profile_settings_form': profile_form})
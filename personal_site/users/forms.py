from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile, TEAM_STATUSES


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=20)
    password = forms.CharField(label='Пароль', max_length=30, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=20)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль', max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', max_length=30, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("Такое имя пользователя уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Такой адрес электронной почты уже существует")
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['email', ]


class UpdateProfileForm(forms.ModelForm):
    profile_name = forms.CharField(label='Имя профиля', widget=forms.TextInput(attrs={'class': 'profile_text_input', 'rows': 1}))
    avatar = forms.ImageField(label='Аватар', widget=forms.FileInput(attrs={'class': 'profile_file_input'}))
    game_account = forms.URLField(label='Игровой аккаунт', widget=forms.URLInput(attrs={'class': 'profile_text_input', 'rows': 1}), required=False)
    team_status = forms.ChoiceField(label='Статус команды', choices=TEAM_STATUSES, widget=forms.Select(attrs={'class': 'profile_choice_field'}))

    class Meta:
        model = Profile
        fields = ['profile_name', 'avatar', 'game_account', 'team_status', ]

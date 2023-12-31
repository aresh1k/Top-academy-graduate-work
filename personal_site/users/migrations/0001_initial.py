# Generated by Django 4.2.2 on 2023-10-07 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=48, verbose_name='Имя профиля')),
                ('avatar', models.ImageField(default='profiles/avatar_default.svg', upload_to=users.models.avatar_directory_path, verbose_name='Аватар')),
                ('game_account', models.URLField(blank=True, max_length=300, null=True, verbose_name='Игровой аккаунт')),
                ('team_status', models.CharField(blank=True, choices=[('Отсутствует', 'Отсутствует'), ('В поиске', 'В поиске'), ('В команде', 'В команде')], max_length=200, null=True, verbose_name='Статус команды')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def avatar_directory_path(instance, filename):
    return 'profiles/{0}/{1}'.format(instance.user.username, filename)


TEAM_STATUSES = (
    ('Отсутствует', 'Отсутствует'),
    ('В поиске', 'В поиске'),
    ('В команде', 'В команде'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    profile_name = models.CharField(max_length=48, verbose_name='Имя профиля')
    avatar = models.ImageField(upload_to=avatar_directory_path, default='profiles/avatar_default.svg', verbose_name='Аватар')
    game_account = models.URLField(max_length=300, null=True, blank=True, verbose_name='Игровой аккаунт')
    team_status = models.CharField(max_length=200, null=True, blank=True, choices=TEAM_STATUSES, verbose_name='Статус команды')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def delete(self, *args, **kwargs):
        profile_data = User.objects.get(id=self.user)
        super().delete(*args, **kwargs)
        Profile.objects.create(user=profile_data.user, profile_name=profile_data.profile_name)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, profile_name=instance.username)

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=48)
    profile_name = models.CharField(max_length=48, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to=f'profiles/{user}', default='profiles/avatar_default.svg')
    game_account = models.CharField(max_length=200, null=True, blank=True)
    team_status = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

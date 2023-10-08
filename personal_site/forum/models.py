from django.db import models
from users.models import User


class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    title = models.CharField(max_length=40, unique=True, verbose_name='Тема')
    content = models.TextField(null=False, blank=False, verbose_name='Содержание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'


class Comment(models.Model):
    theme = models.ForeignKey(Discussion, on_delete=models.CASCADE, verbose_name='Тема обсуждения')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    content = models.TextField(null=False, blank=False, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.theme.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

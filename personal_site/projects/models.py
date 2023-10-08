from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Содержание')
    link = models.CharField(max_length=200, unique=True, verbose_name='Ссылка')
    preview_image = models.ImageField(upload_to=f'articles/', default='articles/post_default.svg', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    link = models.CharField(max_length=200, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to=f'projects/', default='projects/project_default.svg', verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'projects/articles/{article}', null=True, blank=True)

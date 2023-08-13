from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    preview_image = models.ImageField(upload_to='projects/articles/', default='projects/project_default.jpg')
    images = models.FileField(upload_to='projects/articles/')
    link = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/', default='projects/project_default.jpg')
    link = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

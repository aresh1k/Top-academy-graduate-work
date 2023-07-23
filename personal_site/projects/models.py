from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='projects/', default='projects/project_default.jpg')
    link = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='projects/articles/', default='projects/project_default.jpg')
    link = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

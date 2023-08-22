from django.shortcuts import render
from .models import Project, Article


def main(request):
    projects_model = Project.objects.all()
    context = {
        'projects': projects_model,
    }

    return render(request, 'projects/main.html', context)


def blog(request):
    posts = Article.objects.all()
    context = {
        'posts': posts,
    }
    last_blogs = Article.objects.all().order_by('-id')[:8]
    if len(last_blogs) >= 8:
        context['last_blogs'] = last_blogs
    return render(request, 'projects/blog.html', context)


def projects(request):
    projects_data = Project.objects.all()
    context = {
        'projects': projects_data,
    }
    last_projects = Project.objects.all().order_by('-id')[:2]
    if len(last_projects) > 1:
        context['last_projects'] = last_projects
    return render(request, 'projects/projects.html', context)

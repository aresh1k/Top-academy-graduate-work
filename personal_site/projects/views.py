from django.shortcuts import render
from .models import Project


def main(request):
    projects_model = Project.objects.all()
    context = {
        'projects': projects_model,
    }

    return render(request, 'projects/main.html', context)


def blog(request):
    return render(request, 'projects/blog.html')


def projects(request):
    return render(request, 'projects/projects.html')

from django.shortcuts import render
from .models import Project, Article


def main(request):
    projects_model = Project.objects.all()
    context = {
        'projects': projects_model,
    }

    return render(request, 'projects/main.html', context)


def blog(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Article.objects.create(images=image)
    images = Article.objects.all()
    return render(request, 'projects/blog.html', {'images': images})


def projects(request):
    return render(request, 'projects/projects.html')

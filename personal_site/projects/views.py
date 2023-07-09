from django.shortcuts import render


def main(request):
    return render(request, 'projects/main.html')


def main(request):
    return render(request, 'projects/blog.html')


def projects(request):
    return render(request, 'projects/projects.html')

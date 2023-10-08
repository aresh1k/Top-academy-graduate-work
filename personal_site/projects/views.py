from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Article, Image
from .forms import ArticleForm, ImageForm
from django.contrib.auth.decorators import login_required
from .utils import paginate


def main(request):
    projects_data = Project.objects.all()
    posts = Article.objects.all()
    context = {
        'projects': projects_data,
        'posts': posts,
    }
    last_posts = Article.objects.all().order_by('-id')[:8]
    if len(last_posts) >= 8:
        context['posts'] = last_posts
    last_projects = Project.objects.all().order_by('-id')[:2]
    if len(last_projects) > 1:
        context['projects'] = last_projects
    return render(request, 'projects/main.html', context)


def blog(request):
    posts = Article.objects.all()
    paginator, data = paginate(request, posts, 4)
    context = {
        'posts': data,
        'custom_range': paginator,
    }
    return render(request, 'projects/blog.html', context)


def blog_post(request, link):
    post = Article.objects.get(link=link)
    context = {
        'post': post,
    }
    return render(request, 'projects/post.html', context)


@login_required
def create_post(request):
    return redirect('main')
    # if request.method == 'POST':
    #     form = ArticleForm(request.POST)
    #     files = request.FILES.getlist('image')
    #     if form.is_valid():
    #         f = form.save(commit=False)
    #         f.save()
    #         for img in files:
    #             Image.objects.create(article=f, image=img)
    #         messages.success(request, 'Новая статья опубликована!')
    #         return redirect('projects/blog.html')
    # else:
    #     form = ArticleForm()
    #     image_form = ImageForm()
    #     return render(request, 'projects/create_post.html', {'form': form, 'image_form': image_form})
    #
    # return render(request, 'projects/create_post.html', {'form': form})


def projects(request):
    projects_data = Project.objects.all()
    paginator, data = paginate(request, projects_data, 4)
    context = {
        'projects': data,
        'custom_range': paginator,
    }
    return render(request, 'projects/projects.html', context)


def project(request, link):
    project_data = Project.objects.get(link=link)
    context = {
        'project': project_data,
    }
    return render(request, 'projects/project.html', context)

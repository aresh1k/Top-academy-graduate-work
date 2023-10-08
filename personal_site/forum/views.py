from django.shortcuts import render, redirect
from .models import Discussion, Comment
from .forms import DiscussionForm, CommentForm
from django.contrib.auth.decorators import login_required
from projects.utils import paginate


def forum(request):
    forum_data = Discussion.objects.all()
    paginator, data = paginate(request, forum_data, 6)
    context = {
        'discussions': data,
        'custom_range': paginator,
    }
    return render(request, 'forum/forum.html', context)


def discussion(request, pk):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            f = form.save(commit=False)
            f.user = request.user
            f.theme = Discussion.objects.get(id=pk)
            f.save()
            return redirect('discussion', pk)

    discussion_data = Discussion.objects.get(id=pk)
    comments = Comment.objects.filter(theme=pk)
    comment_form = CommentForm()

    context = {
        'discussion': discussion_data,
        'comments': comments,
        'form': comment_form,
    }

    return render(request, 'forum/discussion.html', context)


@login_required
def create_theme(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('forum')
        
    form = DiscussionForm()

    return render(request, 'forum/create_discussion.html', {'form': form})

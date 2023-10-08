from django import forms
from .models import Discussion, Comment


class DiscussionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'discussion_title', 'rows': 1, 'maxlength': 50}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'discussion_content', 'rows': 3}))

    class Meta:
        model = Discussion
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'discussion_content', 'rows': 3}), label='Комментарий')

    class Meta:
        model = Comment
        fields = ['content']

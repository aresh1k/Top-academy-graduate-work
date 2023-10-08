from django import forms
from .models import Article


class ArticleForm(forms.Form):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'preview_image',
            'link',
        ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}),
        required=False,
    )

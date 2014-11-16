from django import forms

from blog.core.models import Article, Blog


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body')


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'tagline')

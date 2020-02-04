from django import forms
from . import models
from pagedown.widgets import PagedownWidget
from django.contrib.auth.forms import UserChangeForm


class CreateArticle(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = models.Home
        fields = ['title', 'category', 'body', 'thumbnail']


class EditPostForm(UserChangeForm):
    body = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = models.Home
        fields = ['title', 'category', 'body', 'thumbnail']


class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = models.Home
        fields = []


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('Name', 'Email', 'Body')

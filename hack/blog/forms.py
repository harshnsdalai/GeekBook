from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'tags')


class SignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class LogIn(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

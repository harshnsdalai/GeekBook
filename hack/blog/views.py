from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from .forms import PostForm, SignUp, LogIn, CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
# Create your views here.


@login_required
def post_list(request):
    # post = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        # 'published_date')
    post = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': post})


@login_required
def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post_detail})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('post_list')# , pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('post_list')# , pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def sign_up(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        # return HttpResponse(form)  # form.POST.get("password1"))

        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = SignUp()
    return render(request, 'blog/register.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('post_list'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        form = LogIn()
    return render(request, 'blog/login.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('log_in')


@login_required
def tag_info(request, tag):
    posts = Post.objects.filter(tags__name__in=[tag])
    return render(request, 'blog/post_list.html', {'posts': posts, 'tag': tag})


@login_required
def tag_search(request):
    if request.method == "GET":
        tag = request.GET.get('tag-name')
        posts = Post.objects.filter(tags__name__in=[tag])
        pvar = True
        return render(request, 'blog/post_list.html', {'posts': posts, 'pvar': pvar,'tag': tag})


@login_required
def post_search(request):
    if request.method == "GET":
        post_name = request.GET.get('post-name') 
        posts = (Post.objects.filter(title__contains=post_name))
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def all_tags(request):
    tags = Tag.objects.all()
    pvar = True
    return render(request, 'blog/all-tags.html', {'tags': tags, 'pvar': pvar})


@login_required
def my_posts(request):
    post = Post.objects.filter(author_id=request.user.id).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': post})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

# In blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from .models import Blog, Comment, Like
from .forms import BlogForm, CommentForm
from django.shortcuts import redirect, get_object_or_404

from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import logout


def home(request):
    return render(request, 'base.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:blog_list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:blog_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

@login_required
def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})


@login_required  # Apply the login_required decorator to restrict access to authenticated users only
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user  # Assign the authenticated user as the comment author
            comment.save()
            return redirect('blog:blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()
    return redirect('blog:blog_detail', blog_id=blog_id) 

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    # Check if the user has already liked the comment
    if not Like.objects.filter(comment=comment, user=request.user).exists():
        # If not, create a new like
        like = Like(comment=comment, user=request.user)
        like.save()

        # Increment the likes count for the comment
        comment.likes_count += 1
        comment.save()
    
    return redirect('blog:blog_detail', blog_id=comment.blog.id)

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            form.save_m2m()  # Save many-to-many relationships (tags)
            return redirect('blog:blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    comments = blog.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('blog:blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'comments': comments, 'form': form})

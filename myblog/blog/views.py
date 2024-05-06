# In blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from .models import Blog, Comment
from .forms import BlogForm, CommentForm




def home_view(request):
    return render(request, 'blog/home.html')


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

def blog_list(request):
    blogs = Blog.objects.all()
    print(blogs,"++++++++++++++++++")
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})

def logout_view(request):
    logout(request)
    return redirect('blog_list') 

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

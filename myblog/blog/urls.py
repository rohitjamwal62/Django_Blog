# In blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.blog_list, name='blog_list'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('add_comment/<int:blog_id>/', views.add_comment, name='add_comment'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('', views.home, name='home'),
    path('blogs/', views.blog_list, name='blog_list'),
    

]

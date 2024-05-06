# In blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('', views.home_view, name='home'),

]

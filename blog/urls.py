from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'blog'  # namespace
urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='blog/login.html'),
        name='login'),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='blog/logout.html'),
        name='logout'),
    path('index/', views.BlogIndex.as_view(), name='index'),
    path('list/', views.BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    path('publish/', views.BlogPublish.as_view(), name='publish'),
]

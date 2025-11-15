from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_member, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Auth routes
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='gym/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', views.home_view, name='home'),
    path('create-script/', views.create_script_view, name='create_script'),
]

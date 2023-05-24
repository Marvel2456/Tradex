from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_view, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]

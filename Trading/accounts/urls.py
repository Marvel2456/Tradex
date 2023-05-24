from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_view, name='index'),
    path('traders/', views.trader_view, name='traders'),
    path('admin_dashboard/', views.dashboard_view, name='admin_dashboard'),
    path('trader_dashboard/', views.trader_dashboard_view, name='trader_dashboard'),
    path('make_trade/', views.make_trade_view, name='make_trade'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

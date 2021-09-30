from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register', views.register, name='register_user'),
    path('company', views.company_page, name='company_page'),
    path('settings', views.settings_page, name='settings_page'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
]

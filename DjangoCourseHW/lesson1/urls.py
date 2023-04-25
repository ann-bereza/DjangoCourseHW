from django.urls import path
from lesson1 import views

urlpatterns = [
    path('', views.index, name="home"),
    path('lesson_1/', views.les_1, name="lesson_1"),
    path('lesson_1_1/', views.les_1_1, name="lesson_1_1"),

]
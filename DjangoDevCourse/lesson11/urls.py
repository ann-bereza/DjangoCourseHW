from django.urls import path
from lesson11 import views

urlpatterns = [
    path('lesson_1/', views.index, name="home"),
    path('lesson_1_1/', views.les_1_1, name="lesson_1_1"),

]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('leia/', views.page, name='leia'),
    path('luke/', views.page, name='luke'),
    path('han/', views.page, name='han'),
    path('tasks/', views.tasks, name='tasks'),
    path('send-file/', views.send_file, name='send_file'),
    path('dune/', views.dune, name='dune'),
    path('exist/', views.existential, name='exist'),
    path('question/<int:question_id>', views.question, name='question'),
    path('file/', views.file_response, name='file_response'),
    path('json/', views.json_response, name='json_response'),
    path('html/', views.html_response, name='html_response'),
    path('text/', views.text_response, name='text_response'),
]

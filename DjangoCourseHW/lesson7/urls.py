from . import views
from django.urls import path

urlpatterns = [
    path('api/ping/', views.PingView.as_view(), name='ping'),
    path('api/local-time/', views.get_local_time, name='get_local_time'),
]

from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
    path('api/reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/', views.ReviewRetrieveUpdateDeleteView.as_view(), name='review-detail'),
    path('api/reviews/title/<str:title>/', views.ReviewByTitleView.as_view(), name='review-by-title'),

]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.view_detail, name='view_detail'),
    path('submit/<int:id>/', views.submit_quiz, name='submit_quiz'),
]
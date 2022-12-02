from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('teacher_add/', views.teacher_add, name='teacher_add')
]
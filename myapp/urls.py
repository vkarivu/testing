from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_input, name='task_input'),
    path('tasks/', views.task_list, name='task_list'),
    path('task_input/', views.task_input, name='task_input'),
    # path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    
]

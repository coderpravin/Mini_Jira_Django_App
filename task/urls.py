from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.project_List, name='project-list'),
    path('project/<int:pk>', views.project_details, name='project-details'),
    
    # api for task
    path('task', views.task_List, name='task-list'),
    path('task/<int:pk>', views.task_details, name='task-details')
    
]

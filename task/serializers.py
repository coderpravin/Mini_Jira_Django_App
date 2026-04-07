from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source = 'created_by.username')
    class Meta:
        model = Project
        fields = ["name", "desc", "created_by"]
        
class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.ReadOnlyField(source ="project.name")
    assigned_username = serializers.ReadOnlyField(source ="assigned_to.username")
    class Meta:
        model = Task
        fields = ["title", "description", "project_name", "assigned_username", "status"]
        
        
        
        

        
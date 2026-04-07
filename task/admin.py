from django.contrib import admin
from .models import Project, Task
# Register your models here.

class adminProject(admin.ModelAdmin):
    list_display = ["name", "desc", "created_at"]
    
admin.site.register(Project, adminProject)

class adminTask(admin.ModelAdmin):
    list_display = ["title", "description", "get_project_name", "get_assigned_username", "status"]

    def get_project_name(self, obj):
        if obj.project:
            return obj.project.name
        return "No Projet"
        
    def get_assigned_username(self, obj):
        if obj.assigned_to:
            return obj.assigned_to.username
        return "No username"
        
admin.site.register(Task, adminTask)
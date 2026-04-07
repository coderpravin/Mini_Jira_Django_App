from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    
    
class Task(models.Model):
    
    STATUS_CHOICE = [
        ("todo", "TODO"),
        ("in_progress", "IN_PROGRESS"),
        ("done", "DONE")
    ]
    
    title = models.CharField(max_length = 200, default="New Task")
    description = models.TextField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default="todo")
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    
    

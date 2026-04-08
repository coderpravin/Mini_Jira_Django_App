from django.shortcuts import render,get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(["GET", "POST"])
def project_List(request):
    
    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
  

@api_view(["GET", "PUT", "DELETE"])
def project_details(request,pk):
    
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response("Data not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == "GET":
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "DELETE":
        project.delete()
        return Response("Data Deleted", status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def task_List(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["PUT", "GET", "DELETE"])
@permission_classes([IsAuthenticated])
def task_details(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        
    except Task.DoesNotExist():
        return Response("Task is not available", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "DELETE":
        task.delete()
        return Response("The Task is deleted", status=status.HTTP_204_NO_CONTENT)
    
    
    #handle kanabn view
def kanban_view(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    
    return render(request, 'kanban.html', context)
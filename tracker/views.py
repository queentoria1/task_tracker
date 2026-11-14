from rest_framework import viewsets
from .models import Task, Project, Comment
from .serializers import TaskSerializer, ProjectSerializer, CommentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    A pure API ViewSet that automatically provides CRUD actions
    for Comment items.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, ProjectViewSet, CommentViewSet

# The router automatically builds standard RESTful routes
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]

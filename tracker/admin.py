from django.contrib import admin
from .models import Project, Task, Comment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Display columns in the admin table
    list_display = ('title', 'project')
    
    # Requirement 1: Search tasks by title
    search_fields = ('title',)
    
    # Requirement 2: Filter tasks by project
    list_filter = ('project',)
    
admin.site.register(Project)
admin.site.register(Comment)

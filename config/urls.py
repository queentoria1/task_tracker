from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin system interface panel URL path
    path('admin/', admin.site.urls),
    
    # Pure REST API data endpoint tracking paths
    path('api/', include('tracker.urls')),
]

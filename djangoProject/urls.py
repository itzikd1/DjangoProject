from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skill/', include('skills.urls', namespace='skill')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('experience/', include('experience.urls', namespace='experience')),
    # path('', include('projects.urls', namespace='projects')),
]

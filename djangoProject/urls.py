from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skills/', include('skills.urls')),
    path('projects/', include('projects.urls')),
    path('experience/', include('experience.urls')),
    # path('', include('projects.urls', namespace='projects')),
]

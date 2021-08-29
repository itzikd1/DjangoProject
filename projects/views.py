from projects.models import Projects
from rest_framework import generics
from .serializers import ProjectsSerializer


# Lead Viewset
class ProjectsListCreate(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

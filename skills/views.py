from skills.models import Skills
from rest_framework import generics
from .serializers import SkillSerializer


# Lead Viewset
class SkillsListCreate(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer

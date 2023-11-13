from rest_framework import viewsets
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

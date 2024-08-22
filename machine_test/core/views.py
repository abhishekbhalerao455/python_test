from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Client, Project
from rest_framework.serializers import  ClientSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def my_projects(self, request):
        projects = Project.objects.filter(users=request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)


from django.shortcuts import render
from rest_framework import viewsets
from .models import TaskItem
from .serializers import TaskItemSerializer


class TaskItemViewset(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all().order_by('priority')
    serializer_class = TaskItemSerializer

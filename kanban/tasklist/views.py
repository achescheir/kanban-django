from django.shortcuts import render
from rest_framework import viewsets
from .models import TaskItem
from .serializers import TaskItemSerializer


class TaskItemViewset(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all().order_by('priority')
    serializer_class = TaskItemSerializer

def show_lists(request):
    context = {
                "backlog": TaskItem.objects.filter(status=TaskItem.BACKLOG).order_by('priority'),
                "ready": TaskItem.objects.filter(status=TaskItem.READY).order_by('priority'),
                "doing": TaskItem.objects.filter(status=TaskItem.DOING).order_by('priority'),
                "done": TaskItem.objects.filter(status=TaskItem.DONE).order_by('priority'),
        }
    return render(request,'display.html',context)

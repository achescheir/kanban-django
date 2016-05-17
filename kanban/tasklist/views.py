from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import TaskItem
from .serializers import TaskItemSerializer
from .forms import TaskItemForm


class TaskItemViewset(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all().order_by('priority')
    serializer_class = TaskItemSerializer

def show_lists(request):
    context = {
                "backlog": TaskItem.objects.filter(status=TaskItem.BACKLOG).order_by('priority'),
                "ready": TaskItem.objects.filter(status=TaskItem.READY).order_by('priority'),
                "doing": TaskItem.objects.filter(status=TaskItem.DOING).order_by('priority'),
                "done": TaskItem.objects.filter(status=TaskItem.DONE).order_by('priority'),
                "form": TaskItemForm()
        }
    return render(request,'display.html',context)

# def edit_list_items(request):
#     if request.method == 'POST':
#         form = TaskItemForm(request.POST)
#         if form.is_valid():
#
#             return HttpResponse("Submitted")
#     else:
#         form = TaskItemForm()
#
#     return render(request, "edit.html", {"form":form})

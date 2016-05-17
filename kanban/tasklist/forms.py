from django.forms import ModelForm
from .models import TaskItem

class TaskItemForm(ModelForm):
    class Meta:
        model = TaskItem
        fields = ['title', 'status',"priority"]

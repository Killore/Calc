from .models import Task, Shablon
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']

class ShablonForm(ModelForm):
    class Meta:
        model = Shablon
        fields = ['zagol', 'texts']

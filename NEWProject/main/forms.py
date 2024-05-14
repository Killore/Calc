from .models import Task, Shablon
from django.forms import ModelForm, widgets, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите задание'}),
                   "task": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите задание'})}

class ShablonForm(ModelForm):
    class Meta:
        model = Shablon
        fields = ['zagol', 'texts']

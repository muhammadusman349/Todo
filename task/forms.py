from django import forms
from .models import TodoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title','description','status','priority','assign_to','due_date']


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['status'] 


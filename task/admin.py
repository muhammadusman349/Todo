from django.contrib import admin
from django.http.request import HttpRequest
from .models import TodoList

# Register your models here.

admin.site.register(TodoList)
# admin.site.register(TodoListFile)


# def has_add_permission(self, request):
#     return False

# def has_change_permission(self, request):
#     return False

# def has_delete_permission(self, request):
#     return False 

# def has_view_permission(self,request):
#     return False
     
            
from django.shortcuts import render
from task .models import TodoList
from task .forms import TodoForm
from django.contrib.auth.decorators import permission_required


# @permission_required("task.view")

def home(request):
    if request.user.is_superuser:
        art_queryset= TodoList.objects.all()
    else:
        art_queryset = TodoList.objects.filter(assign_to= request.user)
    context = {"dataset":art_queryset}
    
    return render(request, 'home.html', context)
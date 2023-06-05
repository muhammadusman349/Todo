from django.shortcuts import get_object_or_404, render,redirect
from .models import TodoList
from .forms import TodoForm,TodoListForm
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required("task.can_create",raise_exception=True)
def task_create(request):
    
    form= TodoForm(request.POST or None)
    context ={
        
        "form":form
    }
    if form.is_valid():
        f=form.save(commit=False)
        f.created_by=request.user
        form.save()
    
        context['form']= form
        return redirect('homelist')
    return render (request,"task/create.html",context=context)


def task_detail(request,id):
    context={}
    context["dataset"]=TodoList.objects.get(id=id)
    return render(request,"task/detail.html",context)



def taskupdateview(request,id):
    context = {}
    obj = get_object_or_404(TodoList,id=id)
    form = TodoListForm(request.POST or None,instance=obj)
    if form.is_valid(): 
        form.save()
        return redirect('homelist')
    context["form"]=form 
    return render(request,"task/update.html",context=context)




from django.shortcuts import render, redirect
from .models import todo

# Create your views here.
def index(request):
    todo_list = todo.objects.all()
    if request.method == 'POST':
        InputThing = request.POST.get('InputThing')
        todo.objects.create(
            todo = InputThing
        )
        return redirect('todo_list:index')

    return render(request, 'todo_list/index.html', {'title': 'Django App', "todo_list": todo_list})

def delete(request, id):
    deletes = todo.objects.get(todo_id=id)
    deletes.delete()
    return redirect('todo_list:index')

def complete(request, id):
    if request.method == 'POST':
        completes = todo.objects.get(todo_id=id)
        complete_value = request.POST.get('complete')
        completes.complete = complete_value
        completes.save()
        return redirect('todo_list:index')
        

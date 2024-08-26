from django.shortcuts import render, redirect
from .models import todo

# Create your views here.
def index(request):
    if request.method == 'POST':
        InputThing = request.POST.get('InputThing')
        todo.objects.create(
            todo = InputThing
        )
        return redirect('todo_list:index')
    
    todo_list = todo.objects.all()  
    return render(request, 'todo_list/index.html', {'title': 'Django App', "lists": todo_list})

def delete(request, id):
    deletes = todo.objects.get(todo_id=id)
    deletes.delete()
    return redirect('todo_list:index')

def complete(request, id):
    completes = todo.objects.get(todo_id=id)
    if request.method == 'POST':
        complete_value = request.POST.get('completed')
        completes.complete = 1 if complete_value else 0
        completes.save()
    return redirect('todo_list:index')

        

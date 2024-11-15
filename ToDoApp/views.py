from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# List all tasks
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

# Create a new task
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'todo_form.html')

# Update an existing task
def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'todo': todo})

# Delete a task
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_confirm_delete.html', {'todo': todo})

def todo_mark_completed(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed  # Toggle the completion status
    todo.save()
    return redirect('todo_list')  # Redirect back to the task list page
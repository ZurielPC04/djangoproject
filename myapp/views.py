from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = 'Django Curso!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'Isai'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" % username)


def numeroId(request, id):
    result = id + 100 * 2
    return HttpResponse("<h2>ID: %s</h2>" % result)


def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request, id):
    task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('tasks: %s' % task.id)
    return render(request, 'tasks/tasks.html', {
        'task': task
    })


def tasks(request, title):
    task = Task.objects.get(title=title)
    # task = get_object_or_404(Task, name=name)
    return HttpResponse('tasks: %s' % task.title)


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/tasks/')


def create_project(request):
    if request.method == "GET":
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        print(request.POST)
        project = Project.objects.create(name=request.POST['name'])
        print(project)
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })

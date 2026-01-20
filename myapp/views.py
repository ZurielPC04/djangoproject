from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewTask

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
    return render(request, 'projects.html',{
        'projects': projects
    })

def tasks(request, id):
    task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('tasks: %s' % task.id)
    return render(request, 'tasks.html')

def tasks(request, tittle):
    task = Task.objects.get(tittle=tittle)
    # task = get_object_or_404(Task, name=name)
    return HttpResponse('tasks: %s' % task.tittle)    

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
    
def create_task(request):
    
    print(request.GET['title'])
    print(request.GET['description'])
    
    return render(request, 'create_task.html', {
        'form': CreateNewTask()
    })
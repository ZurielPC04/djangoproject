from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.

def index(request):
    return HttpResponse("Index Page")

def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" % username)

def numeroId(request, id):
    result = id + 100 * 2
    return HttpResponse("<h2>ID: %s</h2>" % result)

def about(request):
    return HttpResponse("<h2>About</h2> <p> This is about page</p>")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = Task.objects.get(id=id) 
    return HttpResponse('tasks: %s' % task.tittle)

    
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('ID/<int:id>', views.numeroId, name="numeroId"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    # path('tasks/<int:id>', views.tasks),
    path('tasks/', views.tasks, name="tasks"),
    path('title/<str:title>', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
]

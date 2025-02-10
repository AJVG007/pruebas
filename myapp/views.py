#from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index (request):
    title="Django Course!!"
    return render(request,"index.html",{
        "title": title
    })

def about(request):
    username = "Jair"
    return render(request,"about.html",{
        "username" : username
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    projects =  Project.objects.all()
    return render(request,"projects/projects.html",{
        "projects" : projects
    })

def tasks(request):
    #task = Task.objects.get(id=id) esta es una manera correcta pero no utilizada la otra nos dara una pagina que ya tiene django
    #task = get_object_or_404(Task, id=id)
    #task = Task.objects.get(id=id)
    #return HttpResponse("tasks %s" % task.id)
    tasks = Task.objects.all()
    return render(request,"tasks/tasks.html",{
        "tasks" : tasks
    })

def create_task(request):
    #print(request.GET['title'])
    #print(request.GET["description"])
    if request.method == "GET":
        #SHOW INTERFACE
        return render(request,"tasks/create_task.html", {
            "form" : CreateNewTask()
        })
    else :
        Task.objects.create(title=request.POST["title"], description=request.POST["description"], project_id=2)
        return redirect("tasks")

def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html",{
            "form": CreateNewProject()
        })
    else:
        #print(request.POST)
        #project = Project.objects.create(name=request.POST["name"])
        #print(project)
        #return render(request, "projects/create_project.html",{
        #    "form": CreateNewProject()
        #})
        Project.objects.create(name=request.POST["name"])
        redirect("projects")

from django.shortcuts import render, HttpResponse
from home.models import Task
def home(request):
    context ={'success' : False}
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        print(title,description)
        ins = Task(TaskTitle=title , TaskDescription = description)
        ins.save()
        context ={'success' : True}
    return render(request, 'index.html',context)

def tasks(request):
    return render(request, 'tasks.html')    

from django.shortcuts import render
from .models import MyProject

def home(request):
    project_list = MyProject.objects.all()
    #return render(request,template_name='home.html',{'projects' : 'project_list'} ) # in .templates/
    return render(request,'home.html',{'project_list':project_list})
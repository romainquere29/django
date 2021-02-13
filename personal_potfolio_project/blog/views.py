from django.shortcuts import render, get_object_or_404
from .models import MyBlog


def home_blogs(request):
    #blog_list = MyBlog.objects.all()
    blog_list = MyBlog.objects.order_by('-date')[:5]
    return render(request, 'all_blogs.html',{'list_of_blogs':blog_list})

def details(request,blog_id):
    blog = get_object_or_404(MyBlog, pk=blog_id)
    return render(request, 'details.html',{'blog':blog})
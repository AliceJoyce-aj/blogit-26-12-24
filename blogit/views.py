from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from . models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogDetails
# Create your views here.
def index(request):
    data = BlogDetails.objects.all()
    return render(request,'index.html',{'result':data})


def create_blog(request):
    if request.method == 'POST':
        blog_title = request.POST.get('blog_title')
        blog_content = request.POST.get('blog_content')
        blog_date = request.POST.get('blog_date')
        data=BlogDetails.objects.create(blog_title=blog_title, blog_content=blog_content, blog_date=blog_date)
        data.save()
    return render(request, 'createblog.html')

def viewbloglist(request):
    data = BlogDetails.objects.all()
    return render(request, 'bloglist.html', {'result': data})

    
def detailedview(request, id):
    data = BlogDetails.objects.get(id=id)
    return render(request, 'detailed_view.html', {'result': data})


def blogdelete(request,id):
    data=BlogDetails.objects.get(pk=id)
    data.delete()
    return redirect('index')


def blogupdate(request, id):
   
    data = get_object_or_404(BlogDetails, id=id)

    if request.method == 'POST':
        blog_title = request.POST.get('blog_title')
        blog_date = request.POST.get('blog_date')
        blog_content = request.POST.get('blog_content')

        
        data.blog_title = blog_title
        data.blog_date = blog_date
        data.blog_content = blog_content
        data.save()

       
        return redirect('detailedview', id=data.id)

    
    return render(request, 'update_blog.html', {'result': data})

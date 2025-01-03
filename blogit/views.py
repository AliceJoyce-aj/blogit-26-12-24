from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from . models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogDetailss
from userapp . models import UserDetails
from . models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

# Create your views here.
# def index(request):
#     uid = request.session.get('uid') 
    
#     if uid:
#         try:
           
#             user = UserDetails.objects.get(id=uid)  
#             blog_author = user.username 
            
          
#             data = BlogDetailss.objects.filter(blog_author=blog_author)
#         except UserDetails.DoesNotExist:
#             data = BlogDetailss.objects.none()  
#     else:
       
#         data = BlogDetailss.objects.all()

#     return render(request, 'index.html', {'result': data})

def create_blog(request):
    uid=request.session.get('uid')
    if request.method == 'POST':
        
        blog_title = request.POST.get('blog_title')
        blog_content = request.POST.get('blog_content')
        blog_date = request.POST.get('blog_date')
        blog_author = request.POST.get('blog_author')  


       
        BlogDetailss.objects.create(
            uid=uid, 
            blog_title=blog_title,
            blog_content=blog_content,
            blog_date=blog_date,
            blog_author=blog_author  
        )
    return render(request, 'createblog.html')


def viewbloglist(request):
    uid = request.session.get('uid')      
    if uid:
        try:
            
            user = UserDetails.objects.get(id=uid)  
            blog_author = user.username  
            
          
            data = BlogDetailss.objects.filter(blog_author=blog_author)
        except UserDetails.DoesNotExist:
            data = BlogDetailss.objects.none()  
    else:
        
        data = BlogDetailss.objects.all()

    return render(request, 'bloglist.html', {'result': data})

def detailedview(request, id):
    data = get_object_or_404(BlogDetailss, id=id)  
    return render(request, 'detailed_view.html', {'result': data})


def blogdelete(request, id):
    uid=request.session.get('uid')
    data = get_object_or_404(BlogDetailss, id=id, uid=uid)
    data.delete()
    return redirect('index')  


def blogupdate(request, id):
    uid=request.session.get('uid')
    data = get_object_or_404(BlogDetailss, id=id, uid=uid)

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

from django.db.models import Q

def index(request):
    uid = request.session.get('uid')  
    query = request.GET.get('q', '')
    if uid:
        try:
            
            user = UserDetails.objects.get(id=uid)  
            blog_author = user.username 
            
            
            data = BlogDetailss.objects.filter(blog_author=blog_author)
        except UserDetails.DoesNotExist:
            
            data = BlogDetailss.objects.none()
    else:
        
        data = BlogDetailss.objects.all()
    
    if query:
        data = data.filter(blog_title__icontains=query)
       
    return render(request, 'index.html', {'result': data, 'query': query})




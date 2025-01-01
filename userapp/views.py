from django.shortcuts import render,redirect,HttpResponse
from . models import *
from .models import UserDetails
from blogit import settings

# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        useremail=request.POST.get("useremail")
        userphone=request.POST.get("userphone")
        userpassword=request.POST.get("userpassword")
        data=UserDetails(username=username,useremail=useremail,userphone=userphone,userpassword=userpassword)
        data.save()
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        useremail = request.POST.get('useremail')
        userpassword = request.POST.get('userpassword')
        
        if UserDetails.objects.filter(useremail=useremail, userpassword=userpassword).exists():
            userdetails = UserDetails.objects.get(useremail=useremail, userpassword=userpassword)
            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.username
            request.session['uemail'] = useremail
            request.session['user'] = 'user'
            
            return render(request, 'index.html', {'status': 'User Login Success'})
        else:
            
            return render(request, 'login.html', {'status': 'Login Failed. Please check your credentials.'})
    
    
    return render(request, 'login.html')


def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect('index')
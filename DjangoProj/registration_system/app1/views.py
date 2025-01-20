from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout #For Authentication and Login
# Create your views here.
def HomePage(request):
    return render (request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password!=password2:
            return HttpResponse("Pass and Confirm Pass are not Same")
        else:
            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST': 
        loginUName=request.POST.get('username')
        loginPass=request.POST.get('pass')
        #Auth user and Store some Data into user
        user=authenticate(request, username=loginUName, password=loginPass)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('USername or password is Incorrect!!')
    return render(request, 'login.html')  

def Logout(request):
    logout(request)
    return redirect('login')
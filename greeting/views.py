from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import movieform,SignupForm,LoginForm
from .models import addshow
from datetime import datetime
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django.db import IntegrityError
# Create your views here.
# def home(request):
#     return render(request,'index.html')


def addshow1(request):
    if request.method=='POST':
        form=movieform(request.POST)
        new_start_time = request.POST.get('start_time')
        new_end_time = request.POST.get('end_time')
        new_screen = request.POST.get('screen')
        
        overlapping_shows = addshow.objects.filter(
        screen=new_screen,
        start_time__lte=new_end_time,
        end_time__gte=new_start_time,
        )
        image = request.POST.get('image')
        
        if overlapping_shows.exists():
            # Print a warning message or handle it as needed
             return HttpResponse("Warning: Multiple shows on the same screen within the start and end time.")
        else:
            if form.is_valid():
            # Save the new show if there's no overlap
             form.save()
            return redirect('home')
        
    else:
     form=movieform()
    return render(request,'addshow.html',{'form':form})

def home(request):
   list=addshow.objects.all()
   screen1=addshow.objects.filter(screen='screen1')
   screen2=addshow.objects.filter(screen='screen2')
   screen3=addshow.objects.filter(screen='screen3')
   unique_start_times = addshow.objects.values('start_time','end_time').distinct()
   return render(request,'index.html',{'list':list,'screen1':screen1,'screen2':screen2,'screen3':screen3,'list2':unique_start_times})
   
   
   
def product_update(request, id):
    product = addshow.objects.get(pk=id)
    if request.method == 'POST':
        form = movieform(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')      
    else:
        form =movieform(instance=product)           
    return render(request, 'update.html', {'form': form})


def product_delete(request,id):
    product=addshow.objects.get(pk=id)  
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'product':product})

def ten(request,start_time):
    list3 = addshow.objects.filter(start_time=start_time)
    return render(request, 'ten.html', {'list3': list3})
    

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        try:
            form = User.objects.create_user(username, email, password)
            return redirect('login')
        except IntegrityError as e:
            return render(request, 'signup.html', {'error': 'username already exists'})
        
    else:
     form=SignupForm() 
    return render(request,'signup.html',{'form':form}) 

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
          user = form.get_user()
          auth_login(request, user)
          return redirect('home')
    else:
      form = AuthenticationForm()
    return render(request, 'login.html', {'form': form}) 



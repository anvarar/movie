from django.shortcuts import render
from .forms import LoginForm
from .models import Customer
def function1(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cust = Customer()
            cust.email = form.cleaned_data['email']
            cust.password = form.cleaned_data['password']
            cust.save()
            return render(request,'form-data.html',{
                 'message':'Data saved to db'
            })
    else:
        form = LoginForm()
    return render(request,'index.html',{'form':form})
def function2(request):
    return render(request,'data1.html') 
def function3(request,title):
    return render(request,'data3.html',{'title':title}) 
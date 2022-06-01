from django.contrib.auth import authenticate, logout
from django.shortcuts import render,redirect


from .forms import moneyform
from.models import money

# Create your views here.


def index(request):
    data=money.objects.all()
    dict={'modata':data}
    return render(request,'index.html',dict)

def create(request):
    if request.method=='POST':
        form=moneyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
        form=moneyform()
    return render(request,'create.html',{'form':form})

def edit(request, name):
   e_data=money.objects.get(name=name)
   form=moneyform(instance=e_data)
   return render(request,"update.html",{'form':form,'name':name})

def update(request,name):
    e_data=money.objects.get(name=name)
    form=moneyform(request.POST,instance=e_data)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request,"update.html",{'form':form,'name':name})

def delete(request,name):
    e_data=money.objects.get(name=name)
    e_data.delete()
    return redirect('/index/')

def login(request):
    if request.method =='POST':
        uname = request.POST.get('uname')
        pwd =request.POST.get('password')
        user = authenticate(username=uname, password=pwd)
        if user:
            return redirect('/index/')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/login/')

def Home(request):
    return render(request,'Home.html')

manikanta



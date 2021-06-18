from django.shortcuts import render, redirect
from .models import Employees
from django.contrib import messages
from django.contrib.auth.models import auth

# Create your views here.

def index(request):
    
    return render(request,'index.html')


def login(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = Employees.objects.get(email=email, password=password )
            if user:
                request.session['user']=user.pk
                request.session['name']=user.name
                request.session['email']=user.email

                request.session['birth_date']=str(user.birth_date)
                return redirect('employee_list')
        except:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
    
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


from .models import Employees

def employee(request):


    sess_id = request.session.get('user', 'mini', )


    sub_ordinates = Employees.objects.filter( work_under = sess_id )  

    context = { 'sub_ordinates' : sub_ordinates  }  

    return render(request, 'employee_1.html', context=context)
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

from admin_app.models import it_fields, related
from super_admin.models import save_data

# Create your views here.
def checker(request):
    dept_field=it_fields.objects.all()
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        departments=request.POST['department']
        deptname=it_fields.objects.get(id=departments)
        if password != c_password:
            return render(request, 'checker.html', {'error': 'Passwords do not match'})
        save_checker=User.objects.create_user(username=username,email=email,password=password,is_superuser=0)
        save_checker.save()
        save_dept=related.objects.create(dept=deptname)
        save_dept.save()

    return render(request,'checker.html',{'dept_field':dept_field})


def checker_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user_log = authenticate(request, username=username, password=password)

        if user_log is not None:
            login(request, user_log)
            
           
            request.session['username'] = user_log.username

            return redirect('checker_page')  
        else:
            return render(request, 'checker_login.html',{'error':'Username or Password not Match'})
    return render(request,'checker_login.html')


def department(request):
    if request.method=="POST":
        dept=request.POST['department']
        savedept=it_fields.objects.create(departments=dept)
        savedept.save()
        return redirect('department')
    return render(request,'department.html')


def checker_page(request):
    return render(request,'checker_page.html')

def maker_list(request):
    checker = request.user
    relationships = save_data.objects.filter(checker_data=checker)
    makers = [relationship.maker_data for relationship in relationships]

    return render(request, 'maker_list.html', {'makers': makers})
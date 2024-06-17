from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

from admin_app.models import it_fields
from maker_app.models import UserDetail
from super_admin.models import save_data
from user_app.models import job_selection


# Create your views here.
def maker(request):
    view_dept=it_fields.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        
        if password != c_password:
            return render(request, 'maker.html', {'error': 'Passwords do not match'})
        save_maker=User.objects.create_user(username=name,email=email,password=password,is_superuser=1)
        save_maker.save()
       
    return render(request,'maker.html',{'view_dept':view_dept})


def maker_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user_log = authenticate(request, username=username, password=password)

        if user_log is not None:
            login(request, user_log)
            
           
            request.session['username'] = user_log.username

            return redirect('maker_page')  
        else:
            return render(request, 'maker_login.html',{'error':'Username or Password not Match'})
    return render(request,'maker_login.html')


def maker_page(request):
   
    return render(request,'maker_page.html')

def applications_received(request):
    details=job_selection.objects.all()
    return render(request,'applications_received.html',{'details':details})

def my_applications(request):
    return render(request,'my_applications.html')


# def approve_user(request, user_id):
#     user = get_object_or_404(UserDetail, id=user_id)
#     user.is_approved = True
#     user.save()
#     return redirect('application_received')
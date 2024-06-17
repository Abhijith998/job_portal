from django.shortcuts import render
from django.contrib.auth.models import User

from admin_app.models import it_fields
from super_admin.models import save_data
# Create your views here.
def super_admin(request):
  
    return render(request,'super_admin.html')


def total_checkers(request):
    view= User.objects.filter(is_superuser='1')
    return render(request,'total_checkers.html',{'view':view})



def total_makers(request):
    view_maker= User.objects.filter(is_superuser='0')
    return render(request,'total_makers.html',{'view_maker':view_maker})


def total_employees(request):
    checker_view= User.objects.filter(is_superuser='0')
    maker_view= User.objects.filter(is_superuser='1')
    if request.method == "POST":
        checker = request.POST['checker']
        checker_details = User.objects.get(id=checker)
        
        maker = request.POST['maker']
        maker_details = User.objects.get(id=maker)
        
        save_datas = save_data.objects.create(
            checker_data=checker_details.username,
            maker_data=maker_details.username
        )
        save_datas.save()

    return render(request,'total_employees.html',{'checker':checker_view,'maker':maker_view})
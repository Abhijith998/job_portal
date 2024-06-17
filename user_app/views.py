from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from admin_app.models import it_fields
from user_app.models import job_selection



def user_page(request):
    jobs_dept=it_fields.objects.all()
    if request.method=="POST":
        dept=request.POST['dept']
        deptname=it_fields.objects.get(id=dept)
        username=request.POST['username']
        state=request.POST['state']
        job_type=request.POST['job_type']
        imge=request.FILES.get('cv')
        save_can=job_selection.objects.create(department=deptname,state=state,job_type=job_type,cv=imge,username=username)
        save_can.save()
   
    return render(request,'user_page.html',{'jobs_dept':jobs_dept})






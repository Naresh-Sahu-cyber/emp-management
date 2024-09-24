from django.shortcuts import render, redirect
from .models import emp
# Create your views here.

def emp_home(request):
    emps= emp.objects.all()

    return render(request, "emp/list.html",{"emps":emps})
def add_emp(request):
    if request.method=="POST":


        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_city=request.POST.get("emp_city")
        emp_address=request.POST.get("emp_address")
        emp_department=request.POST.get("emp_department")
        emp_working=request.POST.get("emp_working")
        emp_phone=request.POST.get("emp_phone")
        #create model object and set the data 

        e=emp()
        e.name= emp_name
        e.emp_id=emp_id
        e.city=emp_city
        e.department=emp_department
    
        e.phone=emp_phone
        e.address=emp_address

        if emp_working is None:
            e.working=False
        else:
            e.working=True    


        # save the data 
        e.save()



        print("coming")
        return redirect("/emp/emp1/")
    return render(request, "emp/add_emp.html",{})
def delete_emp(request,emp_id):
    Emp=emp.objects.get(pk=emp_id)
    Emp.delete()
    return redirect('/emp/emp1/')
def update_emp(request,emp_id):
    Emp=emp.objects.get(pk=emp_id)

    return render(request, "emp/emp_update.html",{'emp':Emp})



from datetime import datetime
from django.shortcuts import render,HttpResponse

from emp_app.models import Employee

# Create your views here.
def index1(request):
    return render(request, 'index1.html')

def all_emp(request):
    emps=Employee.objects.all()
    context = {
        'emps' : emps
        }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method=="POST":
        print("yes")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        dept=request.POST.get("dept")
        salary=request.POST.get("salary")
        bonus=request.POST.get("bonus")
        role=request.POST.get("role")
        phone=request.POST.get("phone")
        
        s=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,
                   role_id=role,phone=phone,hire_date=datetime.now())
        s.save()
        return HttpResponse("Employee added sucessfully")           
    elif request.method=="GET":
         print("get")    
         return render(request, 'add_emp.html')
    else:
             
         return HttpResponse("Handle any exception")    

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_removed=Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse("Employee removed sucessfully")
        except:
            return HttpResponse("Please enter a valid employee id")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    return render(request, 'filter_emp.html')


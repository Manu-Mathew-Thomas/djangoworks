from django.shortcuts import render

from django.shortcuts import render,redirect
from employee.models import Employeedetails

def viewemployee(request):
    if(request.method=="GET"):
        e=Employeedetails.objects.all()
        context={'employee':e}
        return render(request,'viewemployee.html',context)

from employee.forms import EmployeeForm
def addemployee(request):
    if(request.method=="POST"):
        form_instance=EmployeeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('employee:viewemployee')
    if(request.method=="GET"):
        form_instance=EmployeeForm()
        context={'form':form_instance}
        return render(request,'addemployee.html',context)
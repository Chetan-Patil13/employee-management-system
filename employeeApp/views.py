from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee,Role,Department
# Create your views here.
from django.db.models import Q
def index(request):
    template='employeeApp/index.html'
    context={}
    return render(request,template,context)

def view(request):
    template='employeeApp/view.html'
    emp=Employee.objects.all()
    context={"employee":emp}
    return render(request,template,context)

def add(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return redirect('/view/')
    elif request.method=="GET":
        template='employeeApp/add.html'
        context={}
        return render(request,template,context)

def remove(request,i=0):
    if i:
        try:
            emp_to_be_removed =Employee.objects.get(id=i)
            emp_to_be_removed.delete()
            return redirect('/view/')
        except:
            return HttpResponse('please enter a valid EMP ID')
    template='employeeApp/remove.html'
    emp = Employee.objects.all()
    context = {"employee": emp}
    return render(request,template,context)


def filter(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {'employee': emps}
        return render(request, 'employeeApp/view.html', context)

    elif request.method == "GET":
        template = 'employeeApp/filter.html'
        context = {}
        return render(request, template, context)
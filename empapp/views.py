from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from datetime import datetime
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request,'index.html')

def allemp(request):
    emp = employee.objects.all()
    return render(request,'allemp.html',{'emp':emp})


def addemp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        newemp=employee(firstname=firstname,lastname=lastname,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hiredate=datetime.now())
        newemp.save()
        # return HttpResponse("Employee added successfully")
        return redirect(allemp)
    elif request.method=='GET':
        return render(request, 'addemp.html')
    else:
        return HttpResponse("An exception occured.Employee is not added")





def removeemp(request,id=0):
    if id:
        try:
            empremove=employee.objects.get(id=id)
            empremove.delete()
            return redirect(removesuccess)
        except:
            return HttpResponse("Please enter a valid employee ID")
    emp = employee.objects.all()

    return render(request,'removeemp.html',{'emp':emp})


def filteremp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emp = employee.objects.all()
        if name:
            emp = emp.filter(Q(firstname__icontains = name) | Q(lastname__icontains = name) )
        if dept:
            emp = emp.filter(dept__name__icontains = dept)
        #     change type of dept field from number to text in filter html page

        if role:
            emp = emp.filter(role__name__icontains=role)
            #     change type of role field from number to text in filter html page


        return render(request,'allemp.html',{'emp':emp})
    elif request.method == 'GET':
        return render(request, 'filteremp.html')
    else:
        return HttpResponse("An exception occured")



def navbar(request):
    return render(request,'navbar.html')


def removesuccess(request):
    return render(request,'removesuccess.html')
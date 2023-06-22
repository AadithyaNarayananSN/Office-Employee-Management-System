from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from datetime import datetime
from django.db.models import Q


# Create your views here.


def home(request):
    return render(request, 'home.html')


def allemp(request):
    emp = employee.objects.all()
    return render(request, 'allemp.html', {'emp': emp})


def addemp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        newemp = employee(firstname=firstname, lastname=lastname, salary=salary, bonus=bonus, phone=phone, dept_id=dept,
                          role_id=role, hiredate=datetime.now())
        newemp.save()
        # return HttpResponse("Employee added successfully")
        return redirect(allemp)
    elif request.method == 'GET':
        return render(request, 'addemp.html')
    else:
        return HttpResponse("Employee is not added")


def removeemp(request, id=0):
    if id:
        try:
            empremove = employee.objects.get(id=id)
            empremove.delete()
            return redirect(removesuccess)
        except:
            return HttpResponse("Please select a valid employee")
    emp = employee.objects.all()

    return render(request, 'removeemp.html', {'emp': emp})


def filteremp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emp = employee.objects.all()
        if name:
            emp = emp.filter(Q(firstname__icontains=name) | Q(lastname__icontains=name))
        if dept:
            emp = emp.filter(dept__name__icontains=dept)
        #     change type of dept field from number to text in filter html page

        if role:
            emp = emp.filter(role__name__icontains=role)
            #     change type of role field from number to text in filter html page

        return render(request, 'allemp.html', {'emp': emp})
    elif request.method == 'GET':
        return render(request, 'filteremp.html')
    else:
        return HttpResponse("An exception occured")


def navbar(request):
    return render(request, 'navbar.html')


def removesuccess(request):
    return render(request, 'removesuccess.html')


# def login(request):
#     if request.method == 'POST':
#         a = loginform(request.POST)
#         if a.is_valid():
#             em = a.cleaned_data['email']
#             cd = a.cleaned_data['code']
#             if em == "manager@gmail.com" and cd == 33355:
#                     return redirect(home)
#             else:
#                 return HttpResponse("Login failed")
#         else:
#             return HttpResponse("not valid")
#     else:
#         return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        a = loginform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['code']
            b = regmodel.objects.all()
            for i in b:
                # nm = i.name
                if i.email == em and i.password == ps:
                    return redirect(home)
                else:
                    return HttpResponse("Login failed")
        else:
            return HttpResponse("Invalid credentials")


    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['name']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['password2']
            mb = a.cleaned_data['mobile']
            ad = a.cleaned_data['address']
            if ps == cp:
                b = regmodel(name=cn, email=em, password=ps, mobile=mb, address=ad)
                b.save()
                return redirect(login)
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Registration failed")
    return render(request, 'register.html')

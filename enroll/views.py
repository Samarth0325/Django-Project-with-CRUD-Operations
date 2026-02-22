from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistration
from .models import Student

# Create your views here.

#This function will add new item and show that item.
@login_required(login_url='login')
def add_show(request): #it is a view of form for creating and validating and reading the data.
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            reg = Student(name=nm, email=em)
            reg.save()
            fm = StudentRegistration()#it shows form blank after adding data to database.
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()

    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})

#This function will Update/Edit data.
@login_required(login_url='login')
def update_data(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi) 
    return render(request, 'enroll/updatestudent.html', {'form':fm})

#This function will delete data.
@login_required(login_url='login')
def delete_data(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
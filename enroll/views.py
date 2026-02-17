from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

#This function will add new item and show that item.
def add_show(request): #it is a view of form for creating and validating and reading the data.
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password'] #if we do not want to save password reduce this line and declared variable in second line.
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()#it shows form blank after adding data to database.
    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})

#This function will delete data.
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
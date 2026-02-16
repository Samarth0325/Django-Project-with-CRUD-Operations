from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
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

    return render(request, 'enroll/addandshow.html', {'form':fm})
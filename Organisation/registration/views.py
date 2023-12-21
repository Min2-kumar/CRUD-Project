from django.shortcuts import render, HttpResponseRedirect
from registration.froms import EmployeeRegistration
from registration.models import User

# this function will work on Create and Retrive
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            cln = User(name=name, email=email,password=password)
            cln.save()
            fm = EmployeeRegistration()
    else:
        fm = EmployeeRegistration()
    emp = User.objects.all()
    return render(request, 'registration/addandshow.html',{'form':fm, 'em':emp})


# this function will work on edit and update
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(instance=pi)
    return render(request, 'registration/updateemp.html', {'form':fm})



# this function will Delete
def del_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
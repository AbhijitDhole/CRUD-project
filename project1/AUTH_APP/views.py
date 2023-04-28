from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  #Built_in registeration form by django
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def signUpView(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/register.html'
    context = {'form': form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    return render(request, template_name, context) 

def loginView(request):
    template_name = 'AUTH_APP/login_temp.html'
    context = {}
    if request.method == "POST":
        u = request.POST.get('un')  #Username and password entered by user
        p = request.POST.get('pw')
        #print(f'USERNAME:{u}---PASSWORD:{p}')
        user = authenticate(username= u, password=p) #used to check if the registered user is same as logged in user
        #print(f"{user}")
        if user is not None:
            login(request, user)
            return redirect('showorder_url')      
    return render(request, template_name, context)


def logoutView(request):
    logout(request)
    return redirect('login_url')
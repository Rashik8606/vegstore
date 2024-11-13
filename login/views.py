from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .form import CustomCreationForm
# Create your views here.


def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def sign_upview(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def logoutview(request):
    logout(request)
    return redirect('login')
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Place
from .models import Team
# Create your views here.


def index(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, 'index.html', {'result': obj, 'result1': obj1})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
                user.save();
                print('User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching!')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# def about(request):
#     return render(request, 'about.html')
#
# def contact(request):
#     return render(request, 'contact.html')
#
# def details(request):
#     return render(request, 'details.html')
#
# def thanks(request):
#     return render(request, 'thanks.html')

# def result(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     sum = x + y
#     diff = x - y
#     prod = x * y
#     quot = x / y
#     return render(request, 'result.html', {'res1':sum, 'res2':diff, 'res3':prod, 'res4':quot})
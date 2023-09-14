from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

def reguserView(request):
    if request.method == 'GET':
        return render(request, 'reguser/reguser.html', {'formuser': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'reguser/reguser.html', {'formuser': UserCreationForm(), 'error': 'Это имя уже используется'})
        else:
            return render(request, 'reguser/reguser.html', {'formuser': UserCreationForm(), 'error': 'Пароли должны совпадать'})


def loginView(request):
    return render(request, template_name='./login/login.html')
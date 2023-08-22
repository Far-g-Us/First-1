import random

from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def passwordView(request):
    newpassword = ''
    length = int(request.GET.get('length'))
    text = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upper'):
        text.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('upper1'):
        text.extend('1234567890')
    if request.GET.get('upper2'):
        text.extend('!@#$%^&*()-_+=;:,."/?\|`~[]{}')
    for i in range(length):
        newpassword += text[random.randint(0, len(text)-1)]
    return render(request, 'password.html', {'newpassword':newpassword})
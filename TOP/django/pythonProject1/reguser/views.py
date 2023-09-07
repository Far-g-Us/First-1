from django.shortcuts import render

# Create your views here.
def reguserView(request):
    return render(request, template_name='./reguser/reguser.html')

def loginView(request):
    return render(request, template_name='./login/login.html')
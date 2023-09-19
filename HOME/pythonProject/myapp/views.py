from django.shortcuts import render, redirect
from myapp.forms import AnketaForm

def anketa_view(request):
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = AnketaForm()
    return render(request, 'anketa.html', {'form': form})

def result_view(request):
    return render(request, 'result.html')


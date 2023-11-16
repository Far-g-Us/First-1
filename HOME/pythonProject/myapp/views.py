import os, uuid
from django.conf import settings
from django.shortcuts import render, redirect

from .forms import AnketaForm


def generate_unique_filename(filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    return new_filename

def form_page(request):
    if request.method == 'POST':
        form = AnketaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cleaned_data = form.cleaned_data
            image = form.cleaned_data['image']
            if image:
                filename = generate_unique_filename(image.name)
                with open(os.path.join(settings.MEDIA_ROOT, filename), 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
            form_data = {
                'image': cleaned_data['image'],
                'first_name': cleaned_data['first_name'],
                'last_name': cleaned_data['last_name'],
                'birth_day': cleaned_data['birth_day'],
                'skill_1': cleaned_data['skill_1'],
                'skill_2': cleaned_data['skill_2'],
                'skill_3': cleaned_data['skill_3'],
                'skill_4': cleaned_data['skill_4'],
                'skill_5': cleaned_data['skill_5'],
                'about_me': cleaned_data['about_me'],
            }
            return render(request, 'result.html', {'form_data': form_data})
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form = AnketaForm()
    return render(request, 'form.html', {'form': form})

def result_view(request):
    return render(request, 'result.html')


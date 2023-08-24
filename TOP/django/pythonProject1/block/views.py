from django.shortcuts import render

# Create your views here.
def blockView(request):
    return render(request, template_name='./block/block.html')
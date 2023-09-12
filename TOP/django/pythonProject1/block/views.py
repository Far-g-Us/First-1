from django.shortcuts import render, get_object_or_404
from.models import Article

# Create your views here.
def blockView(request):
    articles = Article.objects.all() #отвечает за хранение подключенной базы
    return render(request, template_name='./block/block.html', context={'articles':articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail/detail.html', {'article_id':article_id})
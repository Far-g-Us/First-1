from django.urls import path
from . import views


urlpatterns = [
    path('', views.blockView, name='block'),
    path('<int:article_id>/', views.detail, name='detail'),
]
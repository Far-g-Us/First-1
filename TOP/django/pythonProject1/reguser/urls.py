from django.urls import path
from .views import *

urlpatterns = [
    path('register/', reguserView, name='reguser'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profileView, name='profile'),
    path('profileup/', profileupView, name='profileup'),
]
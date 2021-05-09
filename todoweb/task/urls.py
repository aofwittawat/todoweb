from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('about', About, name='about'),
    path('addproject', Addproject, name='addproject'),
    path('addtask', Addtask, name='addtask'),
]

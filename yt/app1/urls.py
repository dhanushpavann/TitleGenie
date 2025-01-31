from django.urls import path
from .views import generate_title

urlpatterns = [
    path('', generate_title, name='generate_title'),
 
]

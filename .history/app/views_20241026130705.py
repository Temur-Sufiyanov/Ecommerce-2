from django.shortcuts import render
from 
# Create your views here.

def home(request):
    
    return render(request, 'app/home.html')
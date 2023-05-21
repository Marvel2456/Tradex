from django.shortcuts import render
from .models import Trade, Trader
from django.contrib.auth.models import User

# Create your views here.



def dashboard(request):
    return render(request, 'accounts/dashboard.html')


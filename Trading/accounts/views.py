from django.shortcuts import render, redirect
from .models import Trade, Trader
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random
from .tasks import update_trade_data
from django.http import JsonResponse

# Create your views here.


def signup_view(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)


# Login traders
def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)


# Logout traders
def logout_view(request):
    logout(request)
    return redirect('login')



@login_required(login_url=('login'))
def welcome_view(request):
    return render(request, 'accounts/index.html')

# only logged in traders can view their dashboards
@login_required(login_url=('login'))
def dashboard_view(request):
    trade = Trade.objects.all()

    context = {
        'trade': trade
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def make_trade(request):
    if request.method == 'POST':
        trader = request.user.trader
        amount = trader.balance
        # Calculate profit/loss based on your trading logic
        profit = []
        loss = []
        if profit_loss > 0:
            profit.append[profit_loss/100]
        elif profit_loss < 0:
            loss.append[profit_loss/100]
        # For example, assuming a random profit/loss between -10 to 10
        profit_loss = round(random.uniform(-10, 10), 2)
        trader.balance += profit_loss
        trader.save()
        Trade.objects.create(trader=trader, amount=amount)

        # Call the Celery task to update trade data and plot the graph
        update_trade_data.delay(trader.id)

        return redirect('trader_dashboard')
    
    context = {
        'profit': profit,
        'loss': loss
    }

    return render(request, 'accounts/trader_dashboard.html', context)

@login_required(login_url=('login'))
def trader_dashboard_view(request):
    trader = request.user.trader
    trade = Trade.objects.filter(trader=trader)
    
    context = {
        'trader': trader,
        'trade': trade
    }
    return render(request, 'accounts/trader_dashboard.html', context)



def get_trade_data(request):
    trader_id = request.user.trader.id
    trade_data = update_trade_data.delay(trader_id).get()

    return JsonResponse(trade_data)
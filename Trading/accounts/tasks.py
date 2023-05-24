import random
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Trade


@shared_task
def update_trade_data(trader_id):
    # Query trades within the last 1 minute
    start_time = timezone.now() - timedelta(minutes=1)
    trades = Trade.objects.filter(timestamp__gte=start_time, trader_id=trader_id).order_by('timestamp')

    # Calculate profit/loss and timestamps for the trades
    timestamps = [trade.timestamp for trade in trades]
    profit_losses = [trade.amount * round(random.uniform(-10, 10), 2) for trade in trades]

    # Return the data as JSON
    return {'timestamps': timestamps, 'profit_losses': profit_losses}
from django.shortcuts import render, HttpResponse
from .models import BitCoin


# Create your views here.
def index(request):
    coin_data = BitCoin.objects.last() or {
        "name": "Bitcoin",
        "price": 0,
        "timestamp": 0,
        "change_24h_high": 0,
        "change_24h_low": 0,
    }
    list_last_12_coins = BitCoin.objects.order_by("-id")[:12] or []
    page = {
        "coin_data": coin_data,
        "list_last_12_coins": list_last_12_coins,
        "percent_change": (coin_data.price - list_last_12_coins[1].price)
        / list_last_12_coins[1].price
        * 100,
    }
    return render(request, "stock/index.html", page)

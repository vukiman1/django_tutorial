from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
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
        "percent_change": (
            (coin_data.price - list_last_12_coins[1].price)
            / list_last_12_coins[1].price
            * 100
            if len(list_last_12_coins) > 1
            else 0
        ),
    }
    return render(request, "stock/index.html", page)


def get_latest_bitcoin(request):
    latest_coin = BitCoin.objects.order_by("-id").first()
    previous_coin = BitCoin.objects.order_by("-id")[1:2].first()

    if latest_coin and previous_coin:
        percent_change = (
            (latest_coin.price - previous_coin.price) / previous_coin.price * 100
        )
    else:
        percent_change = 0

    data = {
        "name": latest_coin.name,
        "price": float(latest_coin.price),
        "timestamp": latest_coin.timestamp,
        "change_24h_high": float(latest_coin.change_24h_high),
        "change_24h_low": float(latest_coin.change_24h_low),
        "percent_change": percent_change,
    }

    return JsonResponse(data)

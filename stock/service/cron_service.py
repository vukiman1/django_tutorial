from todo_app.settings import settings
from stock.service.api import get_data_from_api
import time

api = settings.API_URL
api_key = settings.API_KEY


def save_bitcoin_data():
    from stock.models import BitCoin

    data = get_data_from_api(api, api_key)
    name = "BTC"
    price = float(data.get("price", 0))
    timestamp = int(data.get("timestamp", int(time.time())))
    change_24h_high = float(data.get("24h_high", 0))
    change_24h_low = float(data.get("24h_low", 0))

    bitcoin = BitCoin.objects.update_or_create(
        timestamp=timestamp,
        defaults={
            "name": name,
            "price": price,
            "change_24h_high": change_24h_high,
            "change_24h_low": change_24h_low,
        },
    )
    return bitcoin

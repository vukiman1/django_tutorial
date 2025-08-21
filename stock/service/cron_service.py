from todo_app.settings import settings
from stock.service.api import get_data_from_api
from stock.models import BitCoin
import time

api = settings.API_URL
api_key = settings.API_KEY


def save_bitcoin_data():
    print("save_bitcoin_data")
    # data = get_data_from_api(api, api_key)
    # name = data.get("name", "Bitcoin")
    # price = float(data.get("price", 0))
    # timestamp = int(data.get("timestamp", int(time.time())))
    # change_24h_high = float(data.get("high_24h", 0))
    # change_24h_low = float(data.get("low_24h", 0))

    # bitcoin = BitCoin.objects.create(
    #     name=name,
    #     price=price,
    #     timestamp=timestamp,
    #     change_24h_high=change_24h_high,
    #     change_24h_low=change_24h_low,
    # )

    # return bitcoin

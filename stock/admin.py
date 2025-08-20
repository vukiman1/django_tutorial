from django.contrib import admin
from .models import BitCoin

admin.site.register(
    BitCoin,
    list_display=("name", "price", "timestamp"),
    list_filter=("name", "timestamp"),
    search_fields=("name", "price"),
)

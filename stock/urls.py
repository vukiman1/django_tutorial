from django.urls import path
from . import views


app_name = "stock"
urlpatterns = [
    path("", views.index, name="index"),
    path("api/bitcoin/latest/", views.get_latest_bitcoin, name="get_latest_bitcoin"),
]

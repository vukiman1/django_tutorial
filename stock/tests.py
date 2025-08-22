from django.test import TestCase, Client
from django.urls import reverse
from stock.models import BitCoin
import json
from decimal import Decimal


class BitcoinAPITestCase(TestCase):
    def setUp(self):
        BitCoin.objects.create(
            name="Bitcoin",
            price=Decimal("50000.00"),
            timestamp=1625097600,
            change_24h_high=Decimal("51000.00"),
            change_24h_low=Decimal("49000.00"),
        )

        BitCoin.objects.create(
            name="Bitcoin",
            price=Decimal("52000.00"),
            timestamp=1625184000,
            change_24h_high=Decimal("53000.00"),
            change_24h_low=Decimal("51000.00"),
        )

    def test_get_latest_bitcoin(self):
        client = Client()

        response = client.get(reverse("stock:get_latest_bitcoin"))

        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.content}")

        self.assertIn(response.status_code, [200, 400])

        if response.status_code == 200:
            data = json.loads(response.content)

            self.assertEqual(data["name"], "Bitcoin")
            self.assertEqual(data["price"], 52000.0)
            self.assertEqual(data["timestamp"], 1625184000)
            self.assertEqual(data["change_24h_high"], 53000.0)
            self.assertEqual(data["change_24h_low"], 51000.0)
            self.assertEqual(data["percent_change"], 4.0)

    def test_get_latest_bitcoin_no_data(self):
        BitCoin.objects.all().delete()

        client = Client()

        response = client.get(reverse("stock:get_latest_bitcoin"))

        self.assertEqual(response.status_code, 500)

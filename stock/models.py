from django.db import models


# Create your models here.
class BitCoin(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.PositiveBigIntegerField(
        db_index=True,
        help_text="Unix epoch (seconds)",
    )
    change_24h_high = models.DecimalField(max_digits=20, decimal_places=8)
    change_24h_low = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return self.name

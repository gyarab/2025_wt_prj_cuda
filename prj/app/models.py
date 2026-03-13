from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.symbol


class Strategy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Trade(models.Model):
    TRADE_TYPE = [
        ("LONG", "Long"),
        ("SHORT", "Short"),
    ]

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.SET_NULL, null=True, blank=True)

    trade_type = models.CharField(max_length=10, choices=TRADE_TYPE)

    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    exit_price = models.DecimalField(max_digits=10, decimal_places=2)

    position_size = models.DecimalField(max_digits=10, decimal_places=2)

    date = models.DateField()

    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.asset} {self.trade_type} ({self.date})"
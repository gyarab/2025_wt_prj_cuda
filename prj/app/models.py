from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20, unique=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ["symbol"]

    def __str__(self):
        return self.symbol


class Strategy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Strategies"

    def __str__(self):
        return self.name


class Trade(models.Model):
    TRADE_TYPE = [
        ("LONG", "Long"),
        ("SHORT", "Short"),
    ]

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("CLOSED", "Closed"),
    ]

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="trades")
    strategy = models.ForeignKey(
        Strategy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="trades"
    )

    trade_type = models.CharField(max_length=10, choices=TRADE_TYPE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="OPEN")

    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    exit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    position_size = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    closed_date = models.DateField(null=True, blank=True)

    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.asset} {self.trade_type} ({self.date})"

    @property
    def current_profit_loss(self):
        if self.asset.current_price is None:
            return None

        if self.trade_type == "LONG":
            return (self.asset.current_price - self.entry_price) * self.position_size
        elif self.trade_type == "SHORT":
            return (self.entry_price - self.asset.current_price) * self.position_size
        return None

    @property
    def realized_profit_loss(self):
        if self.exit_price is None:
            return None

        if self.trade_type == "LONG":
            return (self.exit_price - self.entry_price) * self.position_size
        elif self.trade_type == "SHORT":
            return (self.entry_price - self.exit_price) * self.position_size
        return None
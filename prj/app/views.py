from decimal import Decimal
from django.shortcuts import render
from .models import Asset, Strategy, Trade


def home(request):
    trades = Trade.objects.select_related("asset", "strategy").all()

    total_profit_loss = Decimal("0.00")
    for trade in trades:
        value = trade.realized_profit_loss
        if value is not None:
            total_profit_loss += value

    context = {
        "assets_count": Asset.objects.count(),
        "strategies_count": Strategy.objects.count(),
        "trades_count": Trade.objects.count(),
        "total_profit_loss": total_profit_loss,
    }
    return render(request, "app/home.html", context)


def asset_list(request):
    assets = Asset.objects.all()
    return render(request, "app/asset_list.html", {"assets": assets})


def strategy_list(request):
    strategies = Strategy.objects.all()
    return render(request, "app/strategy_list.html", {"strategies": strategies})


def trade_list(request):
    trades = Trade.objects.select_related("asset", "strategy").all()
    return render(request, "app/trade_list.html", {"trades": trades})
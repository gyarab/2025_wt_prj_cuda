from django.contrib import admin
from .models import Asset, Strategy, Trade


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("id", "symbol", "name", "current_price")
    search_fields = ("symbol", "name")
    ordering = ("symbol",)


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "asset",
        "strategy",
        "trade_type",
        "status",
        "entry_price",
        "exit_price",
        "position_size",
        "date",
        "closed_date",
        "get_current_profit_loss",
        "get_realized_profit_loss",
    )
    list_filter = ("trade_type", "status", "date", "closed_date", "asset", "strategy")
    search_fields = ("asset__symbol", "asset__name", "strategy__name", "notes")
    ordering = ("-date",)
    list_select_related = ("asset", "strategy")

    @admin.display(description="Current P/L")
    def get_current_profit_loss(self, obj):
        return obj.current_profit_loss

    @admin.display(description="Realized P/L")
    def get_realized_profit_loss(self, obj):
        return obj.realized_profit_loss
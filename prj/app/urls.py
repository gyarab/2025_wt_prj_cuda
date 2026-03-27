from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("assets/", views.asset_list, name="asset_list"),
    path("strategies/", views.strategy_list, name="strategy_list"),
    path("trades/", views.trade_list, name="trade_list"),
]
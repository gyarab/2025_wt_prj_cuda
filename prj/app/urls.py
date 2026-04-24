from django.urls import path
from . import views
from app.api import api

urlpatterns = [
    path("", views.home, name="home"),
    path("assets/", views.asset_list, name="asset_list"),
    path("strategies/", views.strategy_list, name="strategy_list"),
    path("trades/", views.trade_list, name="trade_list"),
]
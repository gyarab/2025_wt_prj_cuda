from ninja import NinjaAPI, Schema
from typing import List, Optional
from django.shortcuts import get_object_or_404
from datetime import date

from .models import Trade, Asset, Strategy

api = NinjaAPI()


class TradeSchema(Schema):
    id: int
    asset: str
    strategy: Optional[str] = None

    trade_type: str
    status: str

    entry_price: float
    exit_price: Optional[float] = None

    position_size: float
    date: date
    closed_date: Optional[date] = None

    notes: Optional[str] = ""

    current_profit_loss: Optional[float] = None
    realized_profit_loss: Optional[float] = None


class TradeCreateSchema(Schema):
    asset_id: int
    strategy_id: Optional[int] = None

    trade_type: str
    status: str

    entry_price: float
    exit_price: Optional[float] = None

    position_size: float
    date: date
    closed_date: Optional[date] = None

    notes: Optional[str] = ""


def trade_to_dict(t: Trade):
    return {
        "id": t.id,
        "asset": t.asset.symbol,
        "strategy": t.strategy.name if t.strategy else None,
        "trade_type": t.trade_type,
        "status": t.status,
        "entry_price": t.entry_price,
        "exit_price": t.exit_price,
        "position_size": t.position_size,
        "date": t.date,
        "closed_date": t.closed_date,
        "notes": t.notes,
        "current_profit_loss": t.current_profit_loss,
        "realized_profit_loss": t.realized_profit_loss,
    }


@api.get("/trade/", response=List[TradeSchema])
def list_trades(request):
    trades = Trade.objects.select_related("asset", "strategy")
    return [trade_to_dict(t) for t in trades]


@api.get("/trade/{trade_id}", response=TradeSchema)
def get_trade(request, trade_id: int):
    t = get_object_or_404(Trade.objects.select_related("asset", "strategy"), id=trade_id)
    return trade_to_dict(t)


@api.post("/trade/", response=TradeSchema)
def create_trade(request, data: TradeCreateSchema):
    asset = get_object_or_404(Asset, id=data.asset_id)

    strategy = None
    if data.strategy_id:
        strategy = get_object_or_404(Strategy, id=data.strategy_id)

    trade = Trade.objects.create(
        asset=asset,
        strategy=strategy,
        trade_type=data.trade_type,
        status=data.status,
        entry_price=data.entry_price,
        exit_price=data.exit_price,
        position_size=data.position_size,
        date=data.date,
        closed_date=data.closed_date,
        notes=data.notes,
    )

    return trade_to_dict(trade)


@api.put("/trade/{trade_id}", response=TradeSchema)
def update_trade(request, trade_id: int, data: TradeCreateSchema):
    trade = get_object_or_404(Trade, id=trade_id)

    trade.asset = get_object_or_404(Asset, id=data.asset_id)

    if data.strategy_id:
        trade.strategy = get_object_or_404(Strategy, id=data.strategy_id)
    else:
        trade.strategy = None

    trade.trade_type = data.trade_type
    trade.status = data.status
    trade.entry_price = data.entry_price
    trade.exit_price = data.exit_price
    trade.position_size = data.position_size
    trade.date = data.date
    trade.closed_date = data.closed_date
    trade.notes = data.notes

    trade.save()

    return trade_to_dict(trade)


@api.post("/asset/{asset_id}/update-price")
def update_price(request, asset_id: int, price: float):
    asset = get_object_or_404(Asset, id=asset_id)
    asset.current_price = price
    asset.save()
    return {"success": True}
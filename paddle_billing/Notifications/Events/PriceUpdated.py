from datetime import datetime

from paddle_billing.Entities.Event                import Event
from paddle_billing.Entities.Events.EventTypeName import EventTypeName
from paddle_billing.Entities.Price                import Price


class PriceUpdated(Event):
    def __init__(
        self,
        event_id:    str,
        event_type:  EventTypeName,
        occurred_at: datetime,
        data:        Price,
    ):
        super().__init__(event_id, event_type, occurred_at, data)

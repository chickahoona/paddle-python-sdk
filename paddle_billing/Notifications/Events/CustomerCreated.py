from datetime import datetime

from paddle_billing.Entities.Customer             import Customer
from paddle_billing.Entities.Event                import Event
from paddle_billing.Entities.Events.EventTypeName import EventTypeName


class CustomerCreated(Event):
    def __init__(
        self,
        event_id:    str,
        event_type:  EventTypeName,
        occurred_at: datetime,
        data:        Customer,
    ):
        super().__init__(event_id, event_type, occurred_at, data)

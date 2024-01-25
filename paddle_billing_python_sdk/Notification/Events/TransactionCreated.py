from datetime           import datetime
from paddle_billing_python_sdk.Entities       import Events
from paddle_billing_python_sdk.Entities.Event import EventTypeName



class TransactionCreated(Events):
    def __init__(self, event_id: str, event_type: EventTypeName, occurred_at: datetime, data: TransactionWithIncludes):
        super().__init__(event_id, event_type, occurred_at, data)
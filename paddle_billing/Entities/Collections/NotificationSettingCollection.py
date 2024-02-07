from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class NotificationSettingCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> NotificationSettingCollection:
        from paddle_billing.Entities.Notification import Notification

        items: list[Notification] = [Notification.from_dict(item) for item in items_data]

        return NotificationSettingCollection(items, paginator)


    def __next__(self):
        return super().__next__()

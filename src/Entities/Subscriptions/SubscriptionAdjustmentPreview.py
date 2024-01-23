from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.TotalAdjustments import TotalAdjustments

from src.Entities.Subscriptions.SubscriptionAdjustmentItem import SubscriptionAdjustmentItem


@dataclass
class SubscriptionAdjustmentPreview:
    transactionId: str
    items:         list[SubscriptionAdjustmentItem]
    totals:        TotalAdjustments


    @staticmethod
    def from_dict(data: dict) -> SubscriptionAdjustmentPreview:
        return SubscriptionAdjustmentPreview(
            transactionId = data['transaction_id'],
            items         = [SubscriptionAdjustmentItem.from_dict(item) for item in data['items']],
            totals        = TotalAdjustments.from_dict(data['totals']),
        )

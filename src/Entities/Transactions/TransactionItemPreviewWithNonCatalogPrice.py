from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Transactions.TransactionNonCatalogPrice            import TransactionNonCatalogPrice
from src.Entities.Transactions.TransactionNonCatalogPriceWithProduct import TransactionNonCatalogPriceWithProduct


@dataclass
class TransactionItemPreviewWithNonCatalogPrice:
    price:           TransactionNonCatalogPrice | TransactionNonCatalogPriceWithProduct
    quantity:        int
    includeInTotals: bool | None


    @staticmethod
    def from_dict(data: dict) -> TransactionItemPreviewWithNonCatalogPrice:
        return TransactionItemPreviewWithNonCatalogPrice(
            price           = data['price'],
            quantity        = data['quantity'],
            includeInTotals = data.get('include_in_totals'),
        )

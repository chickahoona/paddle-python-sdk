from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CustomData        import CustomData
from src.Entities.Shared.Money             import Money
from src.Entities.Shared.PriceQuantity     import PriceQuantity
from src.Entities.Shared.TaxMode           import TaxMode
from src.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class SubscriptionNonCatalogPrice:
    description:        str
    name:               str | None
    productId:          str
    taxMode:            TaxMode
    unitPrice:          Money
    unitPriceOverrides: list[UnitPriceOverride]
    quantity:           PriceQuantity
    customData:         CustomData | None


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNonCatalogPrice:
        return SubscriptionNonCatalogPrice(
            description        = data['description'],
            name               = data.get('name'),
            productId          = data['productId'],
            taxMode            = TaxMode(data['tax_mode']),
            unitPrice          = Money.from_dict(data['unit_price']),
            unitPriceOverrides = [UnitPriceOverride.from_dict(override) for override in data['unit_price_overrides']],
            quantity           = PriceQuantity.from_dict(data['quantity']),
            customData         = CustomData(data['custom_data']) if 'custom_data' in data else None,
        )

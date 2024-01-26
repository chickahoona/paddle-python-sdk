from paddle_billing_python_sdk.Entities.Shared.Action           import Action
from paddle_billing_python_sdk.Entities.Shared.StatusAdjustment import StatusAdjustment

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager


class ListAdjustments:
    def __init__(
        self,
        pager:            Pager | None                           = None,
        ids:              list[str]                              = None,
        statuses:         list[StatusAdjustment]                 = None,
        customer_ids:     list[str]                              = None,
        transaction_ids:  list[str]                              = None,
        subscription_ids: list[str]                              = None,
        action:           Action | None                          = None,
    ):
        self.pager            = pager
        self.ids              = ids              if ids              is not None else []
        self.statuses         = statuses         if statuses         is not None else []
        self.customer_ids     = customer_ids     if customer_ids     is not None else []
        self.transaction_ids  = transaction_ids  if transaction_ids  is not None else []
        self.subscription_ids = subscription_ids if subscription_ids is not None else []
        self.action           = action

        # Validation
        for field_name, field_value, field_type in [
            ('ids',              self.ids,              str),
            ('customer_ids',     self.customer_ids,     str),
            ('statuses',         self.statuses,         StatusAdjustment),
            ('subscription_ids', self.subscription_ids, str),
            ('transaction_ids',  self.transaction_ids,  str),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException(field_name, field_type.__name__, invalid_items)


    def get_parameters(self) -> dict:
        enum_stringify = lambda enum: enum.value  # noqa E731

        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.customer_ids:
            parameters['customer_id'] = ','.join(self.customer_ids)
        if self.transaction_ids:
            parameters['transaction_id'] = ','.join(self.transaction_ids)
        if self.subscription_ids:
            parameters['subscription_id'] = ','.join(self.subscription_ids)
        if self.action:
            parameters['action'] = self.action.value

        return parameters

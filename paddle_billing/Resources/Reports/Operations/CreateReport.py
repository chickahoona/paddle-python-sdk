from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import ReportType, ReportFilters

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


@dataclass
class CreateReport:
    type:    ReportType
    filters: list[ReportFilters] = field(default_factory=list)


    def __post_init__(self):
        # Validation
        if any(not isinstance(filter_item, ReportFilters) for filter_item in self.filters):
            invalid_items = [filter_item for filter_item in self.filters if not isinstance(filter_item, ReportFilters)]
            raise InvalidArgumentException('filters', 'ReportFilters', ', '.join(map(str, invalid_items)))


    def get_parameters(self) -> dict:
        parameters = {'type': self.type}

        if self.filters is not None and self.filters != []:
            parameters.update({'filters': [filter_.get_parameters() for filter_ in self.filters]})

        return parameters

from src.Entities.EventType import EventType

from src.Entities.Collections.Collection import Collection


class EventTypeCollection(Collection):
    @classmethod
    def from_list(cls, items_data, paginator=None):
        items = [EventType.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()

import uuid
from typing import Dict, Any

from rentomatic.shared.domain_model import DomainModel


class StorageRoom(object):

    def __init__(self, code: uuid.UUID, size: int, price: int, latitude: float, longitude: float) -> None:
        self.code = code
        self.size = size
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_dict(cls, adict: Dict[str, Any]):
        room = StorageRoom(
            code=adict['code'],
            size=adict['size'],
            price=adict['price'],
            latitude=adict['latitude'],
            longitude=adict['longitude'],
        )

        return room

    def to_dict(self) -> Dict[str, Any]:
        return {
            'code': self.code,
            'size': self.size,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }

    def __eq__(self, other):
        if not isinstance(other, StorageRoom):
            return NotImplemented
        return self.to_dict() == other.to_dict()


DomainModel.register(StorageRoom)

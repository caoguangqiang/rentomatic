import json

from rentomatic.domain.storageroom import StorageRoom
import uuid

class StorageRoomEncoder(json.JSONEncoder):

    def default(self, o: StorageRoom) -> dict:
        try:
            to_serialize = {
                'code': str(o.code),
                'size': o.size,
                'price': o.price,
                "latitude": o.latitude,
                "longitude": o.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)

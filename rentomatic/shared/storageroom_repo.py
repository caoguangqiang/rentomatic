from typing import Optional

class StorageRoomRepo:
    def list(self, filters: Optional[dict] = None) -> list:
        raise NotImplementedError
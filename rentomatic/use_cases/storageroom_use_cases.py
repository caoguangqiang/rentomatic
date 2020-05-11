from typing import List

from rentomatic.use_cases.request_objects import StorageRoomListRequestObject
from rentomatic.shared import storageropm_repo as repo
from rentomatic.domain.storageroom import StorageRoom
from rentomatic.shared import use_case as uc
from rentomatic.shared import response_object as res


class StorageRoomListUseCase(uc.UseCase):

    def __init__(self, repo: repo.StorageRoomRepo) -> None:
        self.repo = repo

    def process_request(self, request_object: StorageRoomListRequestObject) -> res.ResponseSuccess:
        domain_storageroom: List[StorageRoom] = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_storageroom)

from abc import ABC, abstractmethod
from typing import Dict

from core.api.dtos import CalculateArrivalTimeResponseSchema


class DBClientSPI(ABC):
    @abstractmethod
    def insert_new_request(self, request_params: CalculateArrivalTimeResponseSchema) -> str:
        """
        Insert new request to the DB and return it ID
        @param request_params: pull all mention requests parameters
        return: id of the DB record
        """

    @abstractmethod
    def get_request_status(self, request_id: str) -> Dict:
        """
        Get status of request
        @param request_id:
        """
        pass

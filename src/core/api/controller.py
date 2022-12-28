from abc import ABC, abstractmethod

from core.api.dtos import (CalculateArrivalTimeResponseSchema,
                           SendTheShipmentResponseSchema)


class VestiaireCollectiveController(ABC):
    """
    Base class for the vestiaire collective handling
    """

    @abstractmethod
    async def send_the_shipment(self) -> SendTheShipmentResponseSchema:
        """
        Calculate the time of shipment arrival to Lunar Colony
        :return: time information about the shipment
        """

    @abstractmethod
    async def calculate_arrival_time(self, request_id: str) -> CalculateArrivalTimeResponseSchema:
        """
        API to get the all information of shipment for the given request_id
        :param request_id: request_id of recently created db instance
        :return: information about the shipment
        """

from core.api.controller import VestiaireCollectiveController
from core.api.dtos import (CalculateArrivalTimeResponseSchema,
                           SendTheShipmentResponseSchema)
from core.impl.utility.arrival_time import ArrivalTimeUtility
from solution.profile import profile


class RestController(VestiaireCollectiveController):

    async def send_the_shipment(self) -> SendTheShipmentResponseSchema:
        """
        Calculate the time of shipment arrival to Lunar Colony
        :return: request_id
        """
        db_params = ArrivalTimeUtility().get_arrival_time()
        request_id = profile.db_client.insert_new_request(db_params)
        return SendTheShipmentResponseSchema(**{"request_id": request_id})

    async def calculate_arrival_time(self, request_id: str) -> CalculateArrivalTimeResponseSchema:
        """
        API to get the all information of shipment for the given request_id
        :param request_id
        :return: CalculateArrivalTimeResponseSchema
        """
        return profile.db_client.get_request_status(request_id)

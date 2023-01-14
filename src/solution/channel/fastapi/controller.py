from fastapi import APIRouter

from core.api.dtos import (CalculateArrivalTimeResponseSchema,
                           SendTheShipmentResponseSchema)
from core.impl.rest_controller import RestController

router = APIRouter(prefix="/core-vestiaire-collective")
rest_controller = RestController()


@router.post(
    "/send_the_shipment",
    status_code=200,
    response_model=SendTheShipmentResponseSchema,
    tags=["Core Vestiaire Collective"],
)
async def sent_the_shipment() -> None:
    """
    Send the shipment from the warehouse
    """
    return await rest_controller.send_the_shipment()


@router.get(
    "/calculate_arrival_time/{request_id}",
    status_code=200,
    response_model=CalculateArrivalTimeResponseSchema,
    tags=["Core Vestiaire Collective"],
)
async def calculate_arrival_time(
    request_id: str,
) -> CalculateArrivalTimeResponseSchema:
    """
    Get calculated time for the shipment by request id
    """
    return await rest_controller.calculate_arrival_time(request_id=request_id)

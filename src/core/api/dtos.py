from datetime import datetime

from pydantic import BaseModel


class SendTheShipmentResponseSchema(BaseModel):
    request_id: str


class ArrivalTimeSchema(BaseModel):
    departure_time_from_warehouse_utc: datetime
    arrival_time_at_earth_space_station_utc: datetime
    arrival_time_at_lunar_colony_utc: datetime
    arrival_time_at_lunar_colony_ltc: str


class CalculateArrivalTimeResponseSchema(BaseModel):
    departure_time_from_warehouse_utc: datetime
    arrival_time_at_earth_space_station_utc: datetime
    arrival_time_at_lunar_colony_utc: datetime
    arrival_time_at_lunar_colony_ltc: str

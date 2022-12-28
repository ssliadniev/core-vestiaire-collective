from datetime import datetime, timedelta

from core.impl.utility.convert_to_lts import LunarStandardTime


class ArrivalTimeUtility:
    def __init__(self):
        self.departure_time = datetime.utcnow()
        self.arrival_time_at_earth_space_station_utc = self.calculate_arrival_time_at_earth_station()
        self.arrival_time_at_lunar_colony_utc = self.calculate_arrival_time_at_lunar_colony()
        self.lunar_time = LunarStandardTime().lunar_datetime()

    def get_arrival_time(self) -> dict:
        shipment_info = {
            "departure_time_from_warehouse_utc": self.departure_time,
            "arrival_time_at_earth_space_station_utc": self.arrival_time_at_earth_space_station_utc,
            "arrival_time_at_lunar_colony_utc": self.arrival_time_at_lunar_colony_utc,
            "arrival_time_at_lunar_colony_ltc": self.lunar_time,
        }
        return shipment_info

    def calculate_arrival_time_at_earth_station(self) -> datetime:
        return self.departure_time + timedelta(days=1)

    def calculate_arrival_time_at_lunar_colony(self) -> datetime:
        return self.arrival_time_at_earth_space_station_utc + timedelta(days=2)

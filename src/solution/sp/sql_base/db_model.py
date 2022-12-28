from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RequestStatus(Base):
    __tablename__ = "request_status"

    id = Column(String(128), primary_key=True, default=lambda: uuid4().hex)
    departure_time_from_warehouse_utc = Column(DateTime, default=lambda: datetime.utcnow())
    arrival_time_at_earth_space_station_utc = Column(DateTime)
    arrival_time_at_lunar_colony_utc = Column(DateTime)
    arrival_time_at_lunar_colony_ltc = Column(String(60), index=True)

import config as conf
import logging

from core.spi.db_client import DBClientSPI
from sqlalchemy import create_engine, update, func
from sqlalchemy.orm import joinedload, sessionmaker
from werkzeug.exceptions import NotFound

from .db_model import RequestStatus

logging.basicConfig(level=logging.DEBUG)


class DBClientSP(DBClientSPI):
    __instance = None
    _engine = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self._engine is None:
            self._engine = create_engine(
                conf.REQUEST_DB_CONNECTION_STRING,
                pool_pre_ping=True,
                pool_recycle=60 * 60
            )
            logging.info(f"Created engine: {self._engine}")
            self._session = sessionmaker(self._engine, future=True, expire_on_commit=False)
            logging.info(f"Session: {self._session}")

    def insert_new_request(self, request_params: dict) -> str:
        """
        Insert new request to the DB and return it ID
        :param request_params: parameters of the request
        :return: id of the DB record

        """
        with self._session() as session:
            with session.begin():
                request = RequestStatus(**request_params)
                session.add(request)
            return request.id

    @staticmethod
    def row_to_dict(row, exclude_keys: tuple = tuple()) -> dict:
        return {
            key: getattr(row, key)
            for key in row.__table__.columns.keys()
            if key not in exclude_keys
        }

    def get_request_status(self, request_id: str) -> dict:
        with self._session() as session:
            query = session.query(RequestStatus)
            query = query.where(RequestStatus.id == request_id).first()
            if query is None:
                raise NotFound(description=f"Can not found request by id {request_id}")
            result = self.row_to_dict(query, exclude_keys=("id", "type"))
            return result

import os
from enum import Enum


HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "6063"))
LOGGER_LEVEL = os.environ.get("LOGGER_LEVEL", "DEBUG").lower()
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"

DB_ENDPOINT = os.environ.get("DB_ENDPOINT", "")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_USERNAME = os.environ.get("DB_USERNAME", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME", "")


class DBType(Enum):
    mysql = "MYSQL"


DB_DRIVERS = {
    DBType.mysql: "mysql"
}

DB_TYPE = DBType(os.environ.get("DB_TYPE", "").upper())
db_driver = DB_DRIVERS[DB_TYPE]

REQUEST_DB_CONNECTION_STRING = (
    f"{db_driver}+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"
)

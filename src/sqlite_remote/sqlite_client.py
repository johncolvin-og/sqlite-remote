import logging.config
from sqlite_rx.client import SQLiteClient
from sqlite_rx import get_default_logger_settings
from sqlite_remote import HTMLViewAdapter


def enable_logging():
    logging.config.dictConfig(get_default_logger_settings(logging.DEBUG))


def create_sql_client(host: str, port: int) -> SQLiteClient:
    """Connect to a sqlite server"""
    return SQLiteClient(connect_address=f"tcp://{host}:{port}")


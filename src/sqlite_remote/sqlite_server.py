import logging.config
from sys import argv
import threading
import socket
from sqlite_rx import get_default_logger_settings
from sqlite_rx.server import SQLiteServer
from sqlite_remote.ArgParser import get_option


def print_help_and_exit(exit_code = 0):
    print(
        """
        Usage: start-sqlite-server.py [OPTIONS] database network-interface

        Positionals:
          database                  Path to the sqlite database file
          network-interface         The network-interface on which to provide service
        
        Options:
          --port                    The port on which to provide service (default 5000)
          --verbose                 Whether or not to print logs to console 
        """
    )
    exit(exit_code)

def next_free_port(port=1024, max_port=65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while port <= max_port:
        try:
            sock.bind(('', port))
            sock.close()
            return port
        except OSError:
            port += 1
    raise IOError('no free ports')


def create_sql_server(
    db_path: str, net_iface: str, preferred_port=5000) -> SQLiteServer:
    """Creates a sqlite server"""
    port = next_free_port(preferred_port)
    return SQLiteServer(
        database=db_path, bind_address=f"tcp://{net_iface}:{port}")


def start_sql_server(
    db_path: str, net_iface: str, preferred_port: 5000) -> SQLiteServer:
    """Creates and starts a sqlite server"""
    server = create_sql_server(db_path, net_iface, preferred_port)
    server.start()
    return server

def main():
    if get_option("--verbose", False):
        logging.config.dictConfig(get_default_logger_settings(logging.DEBUG))
    try:
        start_sql_server(argv[1], argv[2], get_option("--port", 5000))
    except:
        print_help_and_exit(1)


if __name__ == '__main__':
    main()

import logging.config
from sys import argv
from sqlite_rx import get_default_logger_settings
from sqlite_rx.server import SQLiteServer


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
    
def get_option(name: str, options = argv[1:], default_value = None) -> str:
    i = 0
    for arg in options:
        if arg == name:
            if len(options) - 1 > i:
                return options[i + 1]
            break
        i += 1
    return default_value

def create_sql_server(
    db_path: str, net_iface: str, port: int) -> SQLiteServer:
    """Creates a sqlite server"""
    return SQLiteServer(
        database=db_path, bind_address=f"tcp://{net_iface}:{port}")

def start_sql_server(
    db_path: str, net_iface: str, port: int) -> SQLiteServer:
    """Creates and starts a sqlite server"""
    server = create_sql_server(db_path, net_iface, port)
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
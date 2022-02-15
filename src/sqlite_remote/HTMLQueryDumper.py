import subprocess
from sqlite_rx.client import SQLiteClient
from sqlite_remote import HTMLViewAdapter
# from sqlite_remote.OptionParser import get_option


class HTMLQueryDumper:
    def __init__(self, host: str, port: int, output_path: str):
        self.server_address = f"tcp://{host}:{port}"
        self.output_path = output_path

    def __create_client(self):
        return SQLiteClient(self.server_address)

    def query_and_dump(self, query: str, launch_viewer=True):
        print(f"output path: {self.output_path}")
        output_handle = open(self.output_path, "w+")
        cli = self.__create_client()
        result = cli.execute(query)
        result_html = HTMLViewAdapter.dictionary_to_html(result.get("items"))
        output_handle.write(str(result_html))
        if launch_viewer:
            subprocess.call(["xdg-open", self.output_path])


def run(args) -> int:
    try:
        query_dumper = HTMLQueryDumper(args[1], args[2], args[3])
        query_dumper.query_and_dump(args[4])
    except:
        return 1
    return 0

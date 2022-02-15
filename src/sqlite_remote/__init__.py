"""
A sqlite client/server model to execute queries on a remote sqlite db and dump
the results to html.
"""

__author__ = "John Colvin"
__description__ = """
A sqlite client/server model to execute queries on a remote sqlite db and dump
the results to html.
"""

import os
import sqlite_remote.sqlite_client as sqlite_client
import sqlite_remote.HTMLViewAdapter as HTMLViewAdapter
import sqlite_remote.cli.ArgParser
import sqlite_remote.HTTPServer
# import sqlite_remote.HTMLQueryDumper as HTMLQueryDumper

basedir = os.path.dirname(os.path.realpath(__file__))

# from sqlite_remote import HTMLQueryDumper

# if __name__ == '__main__':
#     print("Hey douche")
#     HTMLQueryDumper.main()

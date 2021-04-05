import logging.config
from sqlite_rx.client import SQLiteClient
from sqlite_rx import get_default_logger_settings


def create_sql_client(
    host: str, port: int, enable_logging=True
) -> SQLiteClient:
    """Connect to a sqlite server"""
    if enable_logging:
        logging.config.dictConfig(get_default_logger_settings(logging.DEBUG))
    client = SQLiteClient(connect_address=f"tcp://{host}:{port}")
    return client


def get_html(rows_name: str) -> str:
    """Gets html representation of a dict (presumably rows)"""
    return ""
    "<table>"
    f"{{% for key, value in {rows_name}.items() %}}"
    "    <tr>"
    "        <th> {{ key }} </th>"
    "        <td {{ value }} </td>"
    "    </tr>"
    "{% endfor %}"
    "</table>"


def get_pretty_html(rows: dict, css_class='') -> str:
    """Pretty prints a dictionary into an HTML table(s)"""
    blah = ( '1', '2', '3')
    if isinstance(rows, str):
        return '<td>' + rows + '</td>'
    s = ['<table ']
    if css_class != '':
        s.append('class="%s"' % (css_class))
    s.append('>\n')
    for key, value in rows.items():
        s.append(
            '<tr>\n  <td valign="top"><strong>%s</strong></td>\n' % str(key)
        )
        if isinstance(value, dict):
            if key == 'picture' or key == 'icon':
                s.append(
                    '  <td valign="top"><img src="%s"></td>\n' %
                    Page.prettyTable(value, css_class)
                )
            else:
                s.append(
                    '  <td valign="top">%s</td>\n' %
                    Page.prettyTable(value, css_class)
                )
        elif isinstance(value, list):
            s.append("<td><table>")
            for i in value:
                s.append(
                    '<tr><td valign="top">%s</td></tr>\n' %
                    Page.prettyTable(i, css_class)
                )
            s.append('</table>')
        else:
            if key == 'picture' or key == 'icon':
                s.append('  <td valign="top"><img src="%s"></td>\n' % value)
            else:
                s.append('  <td valign="top">%s</td>\n' % value)
        s.append('</tr>\n')
    s.append('</table>')
    return '\n'.join(s)

class HTML:
    def __init__(self, Header, tableStyles={}, trStyles={}, thStyles={}):
        self.tableStyles = HTML._style_converter(tableStyles)
        trStyles = HTML._style_converter(trStyles)
        thStyles = HTML._style_converter(thStyles)
        self.rows = []
        self.Header = f'<tr {trStyles} >'
        for th in Header:
            self.Header += f'\n<th {thStyles} >{th}</th>'
        self.Header += '\n</tr>'

    @staticmethod
    def _style_converter(styleDict: dict):
        if styleDict == {}:
            return ''
        styles = ''
        for [style, value] in styleDict.items():
            styles += f'{style}: {value};'
        return f'style="{styles}"'

    def add_row(self, row, trStyles={}, tdStyles={}):
        trStyles = HTML._style_converter(trStyles)
        tdStyles = HTML._style_converter(tdStyles)
        temp_row = f'\n<tr {trStyles} >'
        for td in row:
            temp_row += f'\n<td {tdStyles} >{td}</td>'
        temp_row += '\n</tr>'
        self.rows.append(temp_row)

    def __str__(self):
        return \
f'''
<table {self.tableStyles} >
{self.Header}
{''.join(self.rows)}
</table>
'''


def dictionary_to_html(dict) -> HTML:
    html = HTML(
        Header=range(0, len(dict)),
        tableStyles={'margin': '3px'},
        trStyles={'background-color': '#7cc3a97d'},
        thStyles={'color': 'white'}
    )
    i = 0
    for row in dict:
        print(row)
        if i % 2 == 0:
            BGC = 'aliceblue'
        else:
            BGC = '#c2d4e4'
        html.add_row(
            row,
            trStyles={'background-color': BGC},
            tdStyles={'padding': '1rem'}
        )
        i += 1
    return html


def get_html_template(rows_name: str) -> str:
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
    blah = ('1', '2', '3')
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

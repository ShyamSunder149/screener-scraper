from prettytable import PrettyTable
from typing import List

def table_view(headers : List[str], data : List[List[str]]) -> None:
    table = PrettyTable()
    table.field_names = headers
    [table.add_row(row) for row in data] 
    print(table)
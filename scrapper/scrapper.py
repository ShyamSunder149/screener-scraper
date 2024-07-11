import requests
from bs4 import BeautifulSoup
from typing import List

import table_display

def get_first_content(script_id : str) -> List[List[str]]:
    url = "https://www.screener.in/company/" + script_id + "/consolidated/"
    webpage = requests.get(url).content
    soup = BeautifulSoup(webpage, 'html.parser')
    elements = soup.find(id='top-ratios').find_all('li')
    headers = [i.find(class_='name').text.replace('\n    \n    ', '').replace('\n    \n  ', '') for i in elements]
    headers.insert(0,  'Script ID')
    data = [i.find(class_='number').text.replace('\n    \n    ', '').replace('\n    \n  ', '') for i in elements]
    data.insert(0, script_id)
    return [headers, data]

def get_table_data(script_id : str) -> List[List[str]] :
    url = "https://www.screener.in/company/" + script_id + "/consolidated/"
    webpage = requests.get(url).content
    soup = BeautifulSoup(webpage, 'html.parser')
    elements = soup.find(id='top-ratios').find_all('li')
    data = [i.find(class_='number').text.replace('\n    \n    ', '').replace('\n    \n  ', '') for i in elements]
    data.insert(0, script_id)
    return data

def get_table_data_multiple(script_ids : List[List[str]]) -> List[List[str]]:
    return [get_table_data(script_id[0]) for script_id in script_ids]
    
def scrap_single(script_id : str) -> None:
    data = get_first_content(script_id)
    table_display.table_view(data[0], data[1:])

def scrap_multiple(script_ids : List[List[str]]) -> None:
    data =  get_table_data_multiple(script_ids[1:])
    headers = get_first_content(script_ids[0][0])
    data.append(headers[1])
    headers = headers[0]
    table_display.table_view(headers, data)

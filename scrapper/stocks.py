from nsetools import Nse

import database
import scrapper

nse = Nse()

def add_stock(script_id : str) -> None:
    if(nse.is_valid_code(script_id)) :
        database.add_stock(script_id)
        return
    print("Provide a valid script ID")
    
def list_stocks() -> None:
    stocks = database.return_all_stocks()
     
    if(not stocks) :
        print('No stocks found')
        return

    [print(stock[0]) for stock in stocks]
    
def check_all() -> None:
    stocks = database.return_all_stocks()
    
    if (not stocks) :
        print('No stocks found')
        return
    
    scrapper.scrap_multiple(stocks)

    

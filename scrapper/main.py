import typer

import setup 

setup.path_setup()

import stocks
import scrapper

app = typer.Typer()

@app.command()
def check_stock(script_id : str) -> None:
    scrapper.scrap_single(script_id)
    
@app.command()
def check_all() -> None:
    stocks.check_all()

@app.command()
def list_stocks() -> None:
    stocks.list_stocks()

@app.command()
def add_stock(script_id : str) -> None:
    stocks.add_stock(script_id)

if __name__ == "__main__" :
    app()
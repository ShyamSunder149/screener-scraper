from tinydb import TinyDB, Query

db = TinyDB('data.json')
stock = Query()

def add_stock(script_id: str) -> None:
    try:
        if db.contains(stock.script_ids.any([script_id])):
            print(f"Stock {script_id} already exists.")
            return
        db.insert({'script_ids': [script_id]})
        print(f"Stock {script_id} added successfully.")
    except Exception as e:
        print(f"Error adding stock {script_id}: {e}")

def remove_stock(script_id: str) -> None:
    try:
        db.update(lambda rec: {'script_ids': [sid for sid in rec.get('script_ids', []) if sid != script_id]}, stock.script_ids.any([script_id]))
        print(f"Stock {script_id} removed successfully.")
    except Exception as e:
        print(f"Error removing stock {script_id}: {e}")

def return_all_stocks() -> None:
    try:
        all_stocks = db.all()
        return [stock.get('script_ids', []) for stock in all_stocks]
    except Exception as e:
        print(f"Error retrieving stocks: {e}")

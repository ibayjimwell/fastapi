from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


inventory = {
    1: {
        "name": "Cornbeef",
        "price": 344.5,
        "brand": "Pure Foods"
    }
}

# Endpoint or the routes
@app.get("/")
def home():
    return {"Data": "Test"}

@app.get("/about")
def about():
    return {"Title": "This is a title", "Content": "This is the content text of the about page"}

@app.get("/item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item that you want to get.")):
    return inventory[item_id]

@app.get("/item")
def get_item(*, item_name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == item_name:
            return inventory[item_id]
    return HTTPException(status_code=404, detail="Item not found.")

@app.post("/item/create/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return HTTPException(status_code=400, detail="Item ID is already exist.")
    
    inventory[item_id] = item
    return inventory[item_id]

@app.put("item/update/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in inventory:
        return HTTPException(status_code=404, detail="Item ID does not exist.")
    
    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        return HTTPException(status_code=404, detail="Item ID does not exist.")
    
    del inventory[item_id]

    




from products import dao
from typing import List


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data):
        return cls(
            id=data[0],  
            name=data[1],  
            description=data[2],  
            cost=data[3],  
            qty=data[4] if len(data) > 4 else 0  
        )


def list_products() -> List[Product]:
    products = dao.list_products()
    return [Product.load(product) for product in products]


def get_product(product_id: int) -> Product:
    product_data = dao.get_product(product_id)
    if product_data is None:
        raise ValueError(f'Product with ID {product_id} not found.')
    return Product.load(product_data)


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)

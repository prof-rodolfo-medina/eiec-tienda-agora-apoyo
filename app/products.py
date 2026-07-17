PRODUCTS = [
    {"id": 1, "name": "Laptop Agora", "price": 14999.0},
    {"id": 2, "name": "Monitor Agora", "price": 4299.0},
    {"id": 3, "name": "Teclado Agora", "price": 899.0},
    {"id": 4, "name": "Mouse Gamer Agora", "price": 1200.0},
]


def list_products() -> list[dict]:
    """Return a copy of the product catalog."""
    return [product.copy() for product in PRODUCTS]


def get_product(product_id: int) -> dict | None:
    """Return one product by id, or None when it does not exist."""
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product.copy()
    return None


def count_products() -> int:
    """Return the number of products in the catalog."""
    return len(PRODUCTS)

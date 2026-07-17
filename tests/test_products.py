from app.products import count_products, get_product, list_products


def test_list_products_returns_catalog():
    products = list_products()
    assert len(products) == 4


def test_get_product_returns_existing_product():
    product = get_product(1)
    assert product is not None
    assert product["name"] == "Laptop Agora"


def test_get_product_returns_none_for_missing_product():
    assert get_product(999) is None


def test_count_products_returns_catalog_size():
    assert count_products() == 4

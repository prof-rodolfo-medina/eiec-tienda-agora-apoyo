from fastapi import FastAPI, HTTPException

from app.products import count_products, get_product, list_products

APP_VERSION = "2.0.0"

app = FastAPI(
    title="Tienda Agora API",
    version=APP_VERSION,
    description="Repositorio didactico para el curso de CI/CD.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/version")
def version() -> dict[str, str]:
    return {"name": "Tienda Agora API", "version": APP_VERSION}


@app.get("/products")
def products() -> list[dict]:
    return list_products()


@app.get("/products/count")
def products_count() -> dict[str, int]:
    return {"count": count_products()}


@app.get("/products/{product_id}")
def product_detail(product_id: int) -> dict:
    product = get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

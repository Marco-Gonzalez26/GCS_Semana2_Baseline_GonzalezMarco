
CATALOG = [
    {"name": "Ferrari 458 Italia 1:18", "brand": "Bburago", "price": 45.00, "stock": 3},
    {"name": "Toyota Supra MK4 1:24", "brand": "Maisto", "price": 28.50, "stock": 1},
    {"name": "Nissan Skyline GT-R R34 1:32", "brand": "Jada Toys", "price": 15.00, "stock": 5},
]


def list_catalog():
    """Devuelve el catálogo de productos disponibles (REQ-001)."""
    return CATALOG


def filter_by_brand(brand):
    """Filtra el catálogo por marca (REQ-002)."""
    return [item for item in CATALOG if item["brand"].lower() == brand.lower()]


def main():
    print("Baseline v1.0 - Módulo de Catálogo EmiToys (práctica GCS)")
    for item in list_catalog():
        print(f"- {item['name']} | {item['brand']} | ${item['price']} | stock: {item['stock']}")


if __name__ == "__main__":
    main()
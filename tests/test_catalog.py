import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import list_catalog, filter_by_brand


def test_catalog_not_empty():
    """El catálogo debe tener al menos un producto (REQ-001)."""
    assert len(list_catalog()) > 0


def test_filter_by_brand():
    """El filtro por marca debe devolver solo productos de esa marca (REQ-002)."""
    result = filter_by_brand("Bburago")
    assert all(item["brand"] == "Bburago" for item in result)


if __name__ == "__main__":
    test_catalog_not_empty()
    test_filter_by_brand()
    print("OK: pruebas básicas del catálogo pasaron correctamente.")

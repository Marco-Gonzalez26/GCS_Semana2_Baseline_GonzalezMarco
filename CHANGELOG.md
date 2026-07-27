# CHANGELOG

## [v1.0] - 27-07-2026 — Baseline v1.0

### Qué incluye la línea base
- `docs/SRS/SRS_v1.md`: 4 requisitos funcionales y 2 no funcionales
- `docs/SDD/SDD_v1.md`: diseño de arquitectura simple (Catálogo → Carrito → Órdenes).
- `src/main.py`: implementación mínima del módulo de catálogo (listado y filtro por marca).
- `tests/test_catalog.py`: pruebas básicas sobre el catálogo.
- `config/config.example`: plantilla de configuración sin credenciales reales.

### Qué está aprobado
- SRS v1.0 y SDD v1.0 revisados y aprobados como base técnica del proyecto.
- Implementación mínima del catálogo (REQ-001, REQ-002) funcional y probada.

### Qué queda pendiente (fuera de esta línea base)
- Implementación de carrito (REQ-003) y órdenes con validación de stock concurrente (REQ-004, RNF-002).
- Integración real con base de datos y pasarela de pago.

### Cómo se verifica
1. Clonar el repositorio y hacer checkout al tag `v1.0`: `git checkout v1.0`.
2. Ejecutar `python src/main.py` y confirmar que el catálogo se imprime sin errores.
3. Ejecutar `python tests/test_catalog.py` y confirmar el mensaje `OK: pruebas básicas del catálogo pasaron correctamente.`
4. Revisar que `docs/SRS/SRS_v1.md` y `docs/SDD/SDD_v1.md` estén marcados como "Aprobado".

## [Unreleased]
- `REQ-007` agregado tras la baseline v1.0 (ver rama `change/REQ-007`).
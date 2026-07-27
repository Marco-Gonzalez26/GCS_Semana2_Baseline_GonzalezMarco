# Especificación de Requisitos de Software (SRS) — v1.0
**Proyecto:** EmiToys 
**Versión:** 1.0
**Estado:** Aprobado (Baseline v1.0)

## Requisitos Funcionales

- **REQ-001**: El sistema debe permitir a los usuarios visualizar un catálogo de autos a escala con nombre, precio, marca y stock disponible.
- **REQ-002**: El sistema debe permitir filtrar el catálogo por marca y por rango de precio.
- **REQ-003**: El sistema debe permitir agregar productos a un carrito de compras.
- **REQ-004**: El sistema debe permitir completar una compra generando una orden asociada al carrito, con validación de stock disponible.

## Requisitos No Funcionales

- **RNF-001 (Rendimiento):** El listado del catálogo debe responder en menos de 2 segundos bajo condiciones normales de carga.
- **RNF-002 (Concurrencia):** El sistema debe evitar la sobreventa de un mismo producto cuando dos usuarios intentan comprar la última unidad disponible de forma simultánea.

## Control de versiones del documento

| Versión | Fecha       | Autor      | Cambio                          |
|---------|-------------|------------|----------------------------------|
| v1.0    | 2026-07-26  | Marco Gonzalez | Versión inicial aprobada (Baseline) |
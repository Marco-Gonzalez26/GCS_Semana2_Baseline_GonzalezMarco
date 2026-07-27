# Documento de Diseño de Software (SDD) — v1.0
**Proyecto:** EmiToys 
**Versión:** 1.0
**Estado:** Aprobado (Baseline v1.0)

## Arquitectura simple

El sistema se organiza en tres componentes principales:

1. **Módulo de Catálogo** — expone el listado de productos y sus filtros
2. **Módulo de Carrito** — gestiona el estado de los productos seleccionados por el usuario
3. **Módulo de Órdenes** — valida stock y confirma la compra

## Componentes

| Componente        | Responsabilidad                                        |
|--------------------|---------------------------------------------------------|
| CatalogService     | Consultar y filtrar productos disponibles.               |
| CartStore          | Mantener en memoria los ítems seleccionados.             |
| OrderService        | Validar stock y registrar la orden de compra.            |

## Decisiones técnicas

- Se adopta una separación por capas catálogo, carrito, órdenes para mantener responsabilidades claras, inspirada en el patrón Feature-Sliced Design usado en el proyecto real de EmiToys.
- El control de stock se maneja de forma centralizada en `OrderService` para reducir el riesgo de condiciones de carrera al confirmar una compra relacionado con RNF-002.

## Control de versiones del documento

| Versión | Fecha       | Autor      | Cambio                          |
|---------|-------------|------------|----------------------------------|
| v1.0    | 2026-07-26  | Marco Gonzalez | Versión inicial aprobada (Baseline) |
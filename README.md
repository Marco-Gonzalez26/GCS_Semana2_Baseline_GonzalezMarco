# Gestión de la Configuración del Software Semana 2 - Marco Gonzalez — Baseline v1.0 Caso: EmiToys

## Objetivo del proyecto
Este repositorio es una práctica académica de la asignatura **Gestión de la Configuración del Software**. Simula, a menor escala, el depósito de elementos de configuración de **EmiToys**, una plataforma de comercio electrónico de autos a escala (diecast). El propósito no es replicar el proyecto real, sino aplicar los fundamentos de GCS: estructura de repositorio, commits trazables y creación de una línea base (Baseline v1.0).

## Estructura del repositorio

/docs
/SRS -> Especificación de requisitos (SRS_v1.md)
/SDD -> Diseño de software (SDD_v1.md)
/src -> Código mínimo versionado (implementación base del catálogo)
/tests -> Casos de prueba iniciales
/config -> Archivo de configuración de ejemplo (sin datos reales)
/scripts -> Scripts auxiliares de apoyo
CHANGELOG.md -> Historial de cambios del proyecto

## Cómo ejecutar
Este es un proyecto mínimo con fines didácticos (no es la app real de EmiToys). El "código" en `/src` es un placeholder en Python que simula el arranque del módulo de catálogo:

```bash
python src/main.py
```

## Cómo se creó la línea base
1. Se definieron y aprobaron los requisitos (`SRS_v1.md`) y el diseño (`SDD_v1.md`).
2. Se agregó el código mínimo versionado en `/src`.
3. Se realizaron los commits siguiendo la convención `tipo: descripción`.
4. Se etiquetó el estado aprobado con `git tag -a v1.0 -m "Baseline v1.0: SRS+SDD approved + minimal build"`.
5. Se publicó como **Release v1.0** en GitHub, documentando qué incluye, qué está aprobado y cómo verificarla.

> Una línea base no es "lo último que tengo", es "lo aprobado y congelado".
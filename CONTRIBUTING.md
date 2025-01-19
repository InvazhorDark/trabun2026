# Guía de contribución

Este repositorio es mantenido por la Dirección Nacional de Estadística. Las entidades
publicadoras envían sus actualizaciones a través de la mesa de ayuda de datos abiertos;
las personas externas pueden reportar errores abriendo una incidencia.

## Reporte de errores en los datos

Indique en la incidencia:

1. Ruta del archivo afectado (por ejemplo `datasets/boletin-economico/2025/semana-07.csv`).
2. Columna y fila (o identificador del registro).
3. Valor observado y valor esperado, con la fuente que lo respalda.

## Convenciones

- Codificación UTF-8 sin BOM, finales de línea LF.
- Separador coma, decimales con punto, fechas en formato ISO 8601 (`AAAA-MM-DD`).
- La primera fila de cada CSV es siempre el encabezado.
- Los nombres de archivo van en minúsculas, sin espacios ni tildes.
- Todo conjunto nuevo debe registrarse en `datasets/catalogo.csv` y documentarse en
  `docs/diccionario-datos.md`.

## Validación

Antes de enviar cambios ejecute:

```bash
python3 scripts/validar_csv.py datasets/
```

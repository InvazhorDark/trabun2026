# Datos Abiertos — República de Aztravia

Repositorio oficial de conjuntos de datos publicados por la **Dirección Nacional de Estadística (DNE)**
de la República de Aztravia en el marco de la Política Nacional de Apertura de Datos (Decreto 118 de 2023).

Los datos se publican en formatos abiertos (CSV, JSON) con codificación UTF-8, separador coma y
punto como separador decimal. Cada conjunto cuenta con su ficha en `docs/diccionario-datos.md`.

## Estructura

```
datasets/
  catalogo.csv                 Índice de todos los conjuntos publicados
  censo/                       Censo Nacional de Población y Vivienda 2024
  presupuesto/                 Presupuesto General de la Nación (asignado / ejecutado)
  boletin-economico/           Boletín semanal de indicadores de coyuntura
  registro-mercantil/          Altas de sociedades en el Registro Mercantil (por lote)
  indicadores/                 Cortes mensuales de indicadores sociales
  comercio-exterior/           Exportaciones e importaciones mensuales por capítulo arancelario
  elecciones/                  Resultados electorales consolidados
docs/                          Metodología, diccionario de datos y política de apertura
scripts/                       Utilidades de validación y generación del catálogo
```

## Uso rápido

```bash
python3 scripts/validar_csv.py datasets/
python3 scripts/generar_catalogo.py > datasets/catalogo.csv
```

## Periodicidad

| Conjunto | Periodicidad | Responsable |
|---|---|---|
| Boletín económico | Semanal | Subdirección de Cuentas Nacionales |
| Registro mercantil | Según lote | Cámara Nacional de Comercio |
| Indicadores sociales | Mensual | Subdirección de Estadísticas Sociales |
| Comercio exterior | Mensual | Dirección de Aduanas |
| Censo | Decenal | DNE |

## Licencia

Los datos se distribuyen bajo la **Licencia de Datos Abiertos de Aztravia v1.0** (ver `LICENSE`).
Se permite su uso, redistribución y transformación citando la fuente: *DNE – Datos Abiertos de Aztravia*.

## Contacto

datosabiertos@dne-aztravia.org · Av. de la República 1240, San Teodoro.

Última revisión general de este documento: 02/03/2026.

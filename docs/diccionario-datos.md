# Diccionario de datos

## censo/censo-2024-provincias.csv

| Columna | Tipo | Descripción |
|---|---|---|
| codigo_provincia | texto | Código DNE de tres letras |
| provincia | texto | Nombre oficial |
| capital | texto | Capital provincial |
| poblacion | entero | Población censada |
| hogares | entero | Hogares particulares |
| viviendas | entero | Viviendas ocupadas |
| superficie_km2 | decimal | Superficie en km² |
| densidad | decimal | Habitantes por km² |

## presupuesto/presupuesto-AAAA.csv

| Columna | Tipo | Descripción |
|---|---|---|
| sector | texto | Sector de gasto |
| entidad | texto | Entidad ejecutora |
| apropiado | entero | Apropiación inicial (millones de aztras) |
| comprometido | entero | Compromisos acumulados |
| pagado | entero | Pagos acumulados |
| fecha_corte | fecha | Fecha de corte de la ejecución |

## boletin-economico/AAAA/semana-NN.csv

| Columna | Tipo | Descripción |
|---|---|---|
| indicador | texto | Nombre del indicador |
| valor | decimal | Valor observado |
| unidad | texto | Unidad de medida |
| variacion_semanal | decimal | Variación porcentual frente a la semana anterior |
| fecha_corte | fecha | Último día de la semana de referencia |
| estado | texto | `provisional` o `definitivo` |

## registro-mercantil/altas/lote-NNNN.csv

| Columna | Tipo | Descripción |
|---|---|---|
| nit | texto | Número de identificación tributaria |
| razon_social | texto | Denominación social |
| codigo_provincia | texto | Provincia del domicilio principal |
| ciiu | texto | Código de actividad económica |
| actividad | texto | Descripción de la actividad |
| capital_suscrito | entero | Capital suscrito en aztras |
| fecha_matricula | fecha | Fecha de matrícula mercantil |
| tipo_registro | texto | `alta` o `corrección` |

## indicadores/AAAA-MM.json

Documento JSON con los cortes mensuales de los indicadores sociales (tasa de desempleo,
pobreza monetaria, cobertura en salud, matrícula escolar) desagregados por provincia.

## comercio-exterior/AAAA-MM.csv

| Columna | Tipo | Descripción |
|---|---|---|
| flujo | texto | `exportacion` o `importacion` |
| capitulo | texto | Capítulo arancelario (2 dígitos) |
| descripcion | texto | Descripción del capítulo |
| socio | texto | País o bloque socio |
| valor_fob_musd | decimal | Valor FOB en miles de dólares |
| peso_neto_t | decimal | Peso neto en toneladas |
| fecha_corte | fecha | Último día del mes |

## elecciones/municipales-2025/resultados.csv

| Columna | Tipo | Descripción |
|---|---|---|
| codigo_provincia | texto | Provincia |
| municipio | texto | Municipio |
| partido | texto | Partido o movimiento |
| votos | entero | Votos válidos |
| porcentaje | decimal | Porcentaje sobre votos válidos |
| electo | texto | `si` si obtuvo la alcaldía |

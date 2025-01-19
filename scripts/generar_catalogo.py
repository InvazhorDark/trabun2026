#!/usr/bin/env python3
"""Genera el catálogo de conjuntos de datos a partir de la estructura de carpetas."""
import csv
import os
import sys

PERIODICIDAD = {
    "boletin-economico": "semanal",
    "registro-mercantil": "por lote",
    "indicadores": "mensual",
    "comercio-exterior": "mensual",
    "censo": "decenal",
    "presupuesto": "anual",
    "elecciones": "por evento",
}


def main(raiz="datasets"):
    salida = csv.writer(sys.stdout, lineterminator="\n")
    salida.writerow(["id", "conjunto", "ruta", "periodicidad", "formato"])
    n = 0
    for carpeta, _, archivos in sorted(os.walk(raiz)):
        for nombre in sorted(archivos):
            if nombre in ("catalogo.csv", "README.md"):
                continue
            n += 1
            rel = os.path.relpath(os.path.join(carpeta, nombre), raiz)
            conjunto = rel.split(os.sep)[0]
            salida.writerow([
                f"DNE-{n:04d}", conjunto, rel.replace(os.sep, "/"),
                PERIODICIDAD.get(conjunto, "única"), nombre.rsplit(".", 1)[-1].upper(),
            ])


if __name__ == "__main__":
    main(*sys.argv[1:])

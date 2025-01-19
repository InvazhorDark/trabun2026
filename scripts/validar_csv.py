#!/usr/bin/env python3
"""Validación básica de los archivos CSV publicados en el repositorio.

Comprueba codificación UTF-8, presencia de encabezado, número constante de columnas
y formato ISO de las columnas que contienen fechas.
"""
import csv
import os
import re
import sys

FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validar(ruta):
    errores = []
    try:
        with open(ruta, encoding="utf-8") as f:
            filas = list(csv.reader(f))
    except UnicodeDecodeError as e:
        return [f"codificación inválida: {e}"]
    if not filas:
        return ["archivo vacío"]
    encabezado = filas[0]
    if any(not h.strip() for h in encabezado):
        errores.append("encabezado con columnas vacías")
    ancho = len(encabezado)
    col_fecha = [i for i, h in enumerate(encabezado) if h.startswith("fecha")]
    for n, fila in enumerate(filas[1:], start=2):
        if len(fila) != ancho:
            errores.append(f"fila {n}: {len(fila)} columnas, se esperaban {ancho}")
            continue
        for i in col_fecha:
            if fila[i] and not FECHA.match(fila[i]):
                errores.append(f"fila {n}: fecha inválida '{fila[i]}' en columna {encabezado[i]}")
    return errores


def main(raiz):
    total = 0
    con_errores = 0
    for carpeta, _, archivos in os.walk(raiz):
        for nombre in sorted(archivos):
            if not nombre.endswith(".csv"):
                continue
            total += 1
            ruta = os.path.join(carpeta, nombre)
            errores = validar(ruta)
            if errores:
                con_errores += 1
                print(f"[ERROR] {ruta}")
                for e in errores[:10]:
                    print(f"        {e}")
    print(f"Archivos revisados: {total}; con errores: {con_errores}")
    return 1 if con_errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "datasets"))

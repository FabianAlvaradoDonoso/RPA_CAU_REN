# -*- coding: utf-8 -*-

import csv
import sys
import time

# Variables inicales
lista_final = []
lista_headers_wrong = []
col_meses = -1
countMes = 0
sueldo = 301000
countRow = 0

try:
    # Parametros de entradas
    ruta_input = sys.argv[1]
    ruta_output = sys.argv[2]

    # Lectura del archivo INPUT
    csvfile = open(ruta_input, 'r')
    reader = csv.reader(csvfile, delimiter=',')

    # Contiene el contenido del header
    i = next(reader)

    # Contiene el contenido total del archivo INPUT
    rest = [row for row in reader]

    # Vereficar donde esta columna "Meses"
    for col in range(0,len(i)):
        header = i[col].strip()

        if header == 'Meses':
            col_meses = col

    # Ver año ultimo año calendario
    anio = i[col_meses+1][-2:]

    # Descartar meses de otro año
    for col in range(0,len(i)):
        header = i[col].strip()

        # Llenar lista con posicion de meses de otro año calendario
        if col > col_meses and not(anio in header):
            lista_headers_wrong.append(col)

    # Recorrer filas
    for row in range(0,len(rest)):
        countMes = 0

        # Recorre columnas
        for col in range(col_meses+1, lista_headers_wrong[0]):
            
            if int(rest[row][col]) >= sueldo * 0.5: countMes += 1
    
        # Si es el la columna correcta y se encontraron mas de 4 sueldo que cumplan las condiciones
        if countMes >= 4:
            lista_final.append(rest[row])
            countRow += 1

    #Cerrar archivo output
    csvfile.close() 

    # Escribir CSV
    csvfile = open(ruta_output, 'w', newline='')
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    # Escribe en el header
    spamwriter.writerow(i)

    # Escribe el contenido
    for fila in lista_final:
        spamwriter.writerow(fila)

    # Cerrar archivo input
    csvfile.close()
    print("Cantidad de datos filtrados: " + str(countRow))

 	# Segundos de deley para comprobar que esta todo correcto
    time.sleep(5)

except:
    print("FALLO SCRIPT")
    time.sleep(5)

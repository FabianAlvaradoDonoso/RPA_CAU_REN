# -*- coding: utf-8 -*-

# sys.argv[1] => "<ruta_input>|<ruta_output>"
# sys.argv[2] => "<sueldo>"

import csv
import sys
import time

# Variables inicales
lista_final = []
lista_headers_wrong = []
col_meses = -1
countMes = 0
sueldo = 0
countRow = 0

try:
    # -- Parametros de entradas --

    # En el argumento 1, vienen las dos rutas (in|out), y se separan en una lista
    argv = sys.argv[1].split("|")

    # Se asigna las rutas correspondientes a la variable correspondiente
    ruta_input = argv[0]
    ruta_output = argv[1]
    
    # Se asigna el valor del argumento 2 en la variable "sueldo"
    sueldo = int(sys.argv[2])

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
    anio = i[col_meses+1][-4:]

    # Descartar meses de otro año
    for col in range(col_meses+1 ,len(i)):
        header = i[col].strip()

        # Obtener año de la columna actual para comparar
        anio_col = i[col][-4:]
        
        # Llenar lista con posicion de meses de otro año calendario
        if anio_col != anio:
            lista_headers_wrong.append(col)

    # for col in range(col_meses+1, len(i)):
    #     if(col not in lista_headers_wrong):
    #         print("Estos Si {}".format(col))

    # Recorrer filas
    for row in range(0,len(rest)):
        countMes = 0

        for col in range(0, col_meses):
            if '\'' in rest[row][col]: rest[row][col] = rest[row][col].replace('\'', '')

        # Recorre columnas
        for col in range(col_meses+1, len(i)):
            
            if col not in lista_headers_wrong and int(rest[row][col]) >= sueldo * 0.5: countMes += 1
    
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

 	# Segundos de delay para comprobar que esta todo correcto
    time.sleep(3)

except:
    print("FALLO SCRIPT")
    time.sleep(3)

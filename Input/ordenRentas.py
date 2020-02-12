# -*- coding: utf-8 -*-

import csv
import sys
import time

# Variables inicales
lista_final = []
lista_headers_wrong = []
lista_temp = []
col_meses = -1
countMes = 0
sueldo = 301000
countRow = 0

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
    lista_temp = []
    header = i[col].strip()

    if "%" not in header and header != "":
        lista_temp.append(col)
        lista_temp.append(header)
        lista_headers_wrong.append(lista_temp)


# # Ver año ultimo año calendario
# anio = i[col_meses+1][-2:]

# # Descartar meses de otro año
# for col in range(0,len(i)):
#     header = i[col].strip()

#     # Llenar lista con posicion de meses de otro año calendario
#     if col > col_meses and not(anio in header):
#         lista_headers_wrong.append(col)
# Recorrer filas
for años in lista_headers_wrong:
    for row in range(0,len(rest)):
        lista_temp = []
        for col in range(len(rest[row])):
            if(col == años[0]):
                lista_temp.append(años[1])
                lista_temp.append(rest[row][0])
                lista_temp.append(rest[row][col])
        lista_final.append(lista_temp)
print(lista_final)
#Cerrar archivo output
csvfile.close() 

# Escribir CSV
csvfile = open(ruta_output, 'w', newline='')
spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

# Escribe el contenido
for fila in lista_final:
    spamwriter.writerow(fila)

# Cerrar archivo input
csvfile.close()
print("Cantidad de datos filtrados: " + str(countRow))

# # Segundos de deley para comprobar que esta todo correcto
# time.sleep(5)
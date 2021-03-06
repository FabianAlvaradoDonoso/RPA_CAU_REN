# -*- coding: utf-8 -*-

import csv
import sys
import time

# Variables inicales
lista_final = []
lista_headers = []
lista_temp = []
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

    if ".5" not in header and header != "":
        lista_temp.append(col)
        lista_temp.append(header)
        lista_headers.append(lista_temp)

# Recorrer solo la columna de los años
for anios in lista_headers:
    # Recorrer por fila
    for row in range(0,len(rest)):
        lista_temp = []
        # Recorrer por columna
        for col in range(len(rest[row])):
            # Si el index de la columna igual a la de los headers
            if(col == anios[0]):
                lista_temp.append(anios[1].replace(".0", ""))
                lista_temp.append(rest[row][0])
                lista_temp.append(rest[row][col].replace(".0", ""))
                countRow += 1
        lista_final.append(lista_temp)

#Cerrar archivo output
csvfile.close() 

# Escribir CSV
# Python 3
if sys.version_info[0] == 3:
    csvfile = open(ruta_output, 'w', newline='')
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# Python 3
if sys.version_info[0] == 2:
    csvfile = open(ruta_output, 'wb')
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

# Escribe el contenido
for fila in lista_final:
    spamwriter.writerow(fila)

# Cerrar archivo input
csvfile.close()
print("Cantidad de datos ordenados: " + str(countRow))

 # Segundos de delay para comprobar que esta todo correcto
time.sleep(3)
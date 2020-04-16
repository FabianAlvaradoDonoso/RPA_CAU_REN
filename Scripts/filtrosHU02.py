# -*- coding: utf-8 -*-

# sys.argv[1] => "<ruta_input>"
# sys.argv[2] => "<ruta_output>"

import csv
import sys
import time

# Variables inicales
cont_columnas = 0
lista_columnas = []
lista_headers = []
lista_final = []
parentesco = -1
flag81 = False
countRow = 0



# Parametros de entradas
ruta_input = sys.argv[1]
ruta_output = sys.argv[2]

# Lectura del archivo INPUT
csvfile = open(ruta_input, 'r')
reader = csv.reader(csvfile, delimiter=';')

# Contiene el contenido del header
i = next(reader)

# Contiene el contenido total del archivo INPUT
rest = [row for row in reader]

# Obtiene el numero de las columas de las que se debe extraer la informacion
for col in range(0,len(i)):
	header = i[col].strip()

	lista_headers.append(header)

	if header == 'Parentesco':
		parentesco = col
	
# Validar que contenga todas las columnas correctas
if 25 == 25:

	# Recorrer filas
	for row in range(0,len(rest)):
		# Reiniciando las variables temporales
		lista_temporal = []
		flag81 = False

		# Recorrer columanas base:
		for col in range(0,len(rest[row])):
			# Agregando a la lista temporal para luego ser filtrado
			lista_temporal.append(rest[row][col].strip())
		# Si en la columna "Parentesco" == 81, se descarta la fila
		if(int(lista_temporal[parentesco]) == 81): flag81 = True
		# Si no es una fila descartada, se agrega a la lista final
		if not flag81: lista_final.append(lista_temporal)
	
	# Cerrar archivo input
	csvfile.close()

	# Escribir CSV (Dependiendo de la version de Python)
	# Python 3
	if sys.version_info[0] == 3:
		csvfile = open(ruta_output, 'w', newline='')
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	# Python 2
	if sys.version_info[0] == 2:
		csvfile = open(ruta_output, 'wb')
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

	# Escribe en el header
	spamwriter.writerow(lista_headers)

	# Escribe el contenido
	for fila in lista_final:
		spamwriter.writerow(fila)
		countRow += 1

	#Cerrar archivo output
	csvfile.close()

	print("OK. Se procesaron " + str(countRow) + " filas en total.")

	# Segundos de delay para comprobar que esta todo correcto
	time.sleep(3)
else:
	# Si no estan todas las columnas requeridas da un error.
	print("ERROR. Algunas columnas no encontradas")
	time.sleep(3)

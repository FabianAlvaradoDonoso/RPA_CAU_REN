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


try:

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

		if header == 'Rut Carga':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Rut Afil':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Nombre Afiliado':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Direccion Particular':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Comuna':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Ciudad':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Fono Part':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Est. Afil':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Nombre Carga':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if header == 'Parentesco':
			lista_columnas.append(col)
			cont_columnas += 1
			parentesco = col
			lista_headers.append(header)
		if header == 'Meses':
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '01/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '02/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '03/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '04/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '05/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '06/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '07/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '08/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '09/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '10/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '11/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)
		if '12/' in header:
			lista_columnas.append(col)
			cont_columnas += 1
			lista_headers.append(header)

	# Validar que contenga todas las columnas correctas
	if cont_columnas == 25:

		# Recorrer filas
		for row in range(0,len(rest)):
			lista_temporal = []

			# Recorrer columanas base:
			for col in range(0,len(lista_columnas)):
					# Descartar todas las filas con PARENTESCO = 81
					if col == parentesco and rest[row][lista_columnas[col]].strip() == 81: flag81 = True
					if not flag81: lista_temporal.append(rest[row][lista_columnas[col]].strip())
			lista_final.append(lista_temporal)

		# Cerrar archivo input
		csvfile.close()

		# Escribir CSV
		csvfile = open(ruta_output, 'w', newline='')
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

except:
 	print("FALLO SCRIPT. Revisar codigo")
 	time.sleep(3)

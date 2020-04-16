import csv
import sys
import time
import os
os.system('pip install xlrd')

import xlrd

filename = sys.argv[1]
fileout = sys.argv[2]

def csv_from_excel():
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('Hoja1')
    your_csv_file = open(fileout, 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_MINIMAL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
    print("Convertido a CSV")

try:
    csv_from_excel()
    time.sleep(3)
except:
    print("ERROR. Revisar Codigo")
    time.sleep(3)
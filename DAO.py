import csv
import mysql.connector
from mysql.connector import Error



# mysql.connector.connect(host='localhost',database='backlogdb',user='root',password='Abcd.1234')


with open('backlog.csv') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    header = ["CCU Cliente DIM",
                "Numero de la Solicitud Madre",
                "Numero Solicitud",
                "Escenarios",
                "Antiguedad Creación"]
    for r in csv_reader:
        if line_count == 0:
            print(header)
            line_count += 1
        else:
            print( r["CCU Cliente DIM"],
                r["Numero de la Solicitud Madre"],
                r["Numero Solicitud"],
                r["Escenarios"],
                r["Antiguedad Creación"],
                "Pendiente")
            line_count += 1
    print(f'Processed {line_count} lines.')
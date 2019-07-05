
import csv
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
 
def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reportes_metricas")
 
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchone()


def insertReport():
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
                
                args = [
                    r["CCU Cliente DIM"],
                    r["Numero de la Solicitud Madre"],
                    r["Numero Solicitud"],
                    r["Escenarios"],
                    r["Antiguedad Creación"],
                    "03-07-2019",
                    "pendiente",
                    "pendiente"]
                query = "insert into reportes_metricas (CCU_Cliente_DIM,Numero_de_la_Solicitud_Madre,Numero_Solicitud,Escenario,antiguedad,fecha_reportada,descripcion_estado,estado) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                
                try:
                    db_config = read_db_config()
                    conn = MySQLConnection(**db_config)

                    cursor = conn.cursor()
                    cursor.execute(query,args)
                    if cursor.lastrowid:
                        print('ID inserted', cursor.lastrowid)
                    else:
                        print('no row inserted')
                    conn.commit()
                except Error as error:
                    print(error)
                finally:
                    cursor.close()
                    conn.close()

                line_count += 1
    
def getFile():
    with open('backlog.csv') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader = csv.DictReader(csv_file)
    return csv_reader

def insertReportMetricasTI(datos):
    
    return True
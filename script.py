#!/usr/bin/python
import pgdb
from config import config
 
def conectar():
    """ Conexión al servidor de pases de datos PostgreSQL """
    conexion = None
    try:
        # Lectura de los parámetros de conexion
        params = config()
 
        # Conexion al servidor de PostgreSQL
        print('Conectando a la base de datos PostgreSQL...')
        conexion = pgdb.connect(**params)
 
        # creación del cursor
        cur = conexion.cursor()
        
        # Ejecución la consulta para obtener la conexión
        print('La version de PostgreSQL es la:')
        cur.execute('SELECT version()')
 
        # Se obtienen los resultados
        db_version = cur.fetchone()
        # Se muestra la versión por pantalla
        print(db_version)
       
        # Cerremos el cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexión finalizada.')
 
 
if __name__ == '__main__':
    conectar()

from conexion_db import obtener_conexion
# Establecer la conexión a la base de datos


# Crear un objeto cursor
conexion=obtener_conexion()
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL ,
        precio REAL NOT NULL,  
        UNIQUE(nombre,precio) 
               )


''')

print("Tabla 'productos' creada exitosamente.")
# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
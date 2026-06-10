import sqlite3

# Establecer la conexión a la base de datos
conexion=sqlite3.connect("productos.db")


# Crear un objeto cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        #codigo_barra TEXT NOT NULL UNIQUE,Este es el único que no se puede repetir 
        nombre TEXT NOT NULL UNIQUE,
        precio REAL NOT NULL   
        # UNIQUE(nombre,precio)  candado combinado
               )


''')


# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
import sqlite3


# Conexión a la base de datos
conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()


# Le pedimos todos los productos
cursor.execute("SELECT * FROM productos")


# Con fetchall() traemos los resultados y los guardamos en una variable
resultados = cursor.fetchall()


# Los mostramos uno por uno
for producto in resultados:
    print(producto)

conexion.close() # Aquí no hace falta .commit() porque no cambiamos nada, solo leímos
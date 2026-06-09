import sqlite3
# Conexión a la base de datos
conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()


cursor.execute('''
    INSERT OR IGNORE INTO productos (nombre, precio)
    VALUES (?, ?)
''', ("Lápiz", 25.50))

cursor.execute('''
    INSERT OR IGNORE INTO productos (nombre, precio)
    VALUES (?, ?)
''', ("Cuaderno", 120.00))

cursor.execute('''

    INSERT OR IGNORE INTO productos (nombre, precio)
    VALUES (?, ?)
''', ("Mochila", 890.99))
print("Productos agregados exitosamente.")


# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
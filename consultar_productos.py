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
    print(f"ID:{producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")



# CONSULTAS CON WHERE
# 1. Ejecutamos la consulta con el filtro del precio
cursor.execute("SELECT * FROM productos WHERE precio > ?", (100,))

# 2. Traemos todos los resultados que cumplieron la condición (¡En su propia línea!)
productos_filtrados = cursor.fetchall() #fetchall significa "Tráeme todo lo que encontraste".

print("\n=== Productos con Precio Mayor a $100 ===")

for producto in productos_filtrados:
    print(f"ID: {producto[0]} Nombre: {producto[1]} Precio {producto[2]:.2f}")



# CONSULTAS USANDO ORDEN BY
# Ordenar los productos por precio (ascendente)
cursor.execute("SELECT * FROM productos ORDER BY precio ASC")

productos_menores=cursor.fetchall()

print("\n=== Productos ordenados de menor a mayor")
for producto in productos_menores:
    print(f"ID: {producto[0]} Nombre: {producto[1]} Precio: {producto[2]:.2f}")













# --- PARTE 3: El cierre definitivo (VA AL FINAL DE TODO) ---
conexion.close()  #  ¡Ahora sí, cerramos al terminar todo el trabajo!
 




from conexion_db import obtener_conexion


conexion=obtener_conexion()
cursor=conexion.cursor()

# DELETE FROM nombre_de_tabla WHERE condicion;


'''
para eliminar un producto en mysql tenemos que hacer lo siguiente 
creamos una variable y le colocamos el nombre de lo que queremos 
eliminar de la siguiente manera nombre_producto="lapiz", se tiene
que escribir como lo tenemos en nuestra bases de datos, usamos el 
cursor que es el que tiene contacto con la base de datos y eso se hace
de la siguiente manera 
cursor.execute("DELETE FROM productos WHERE nombre = ?",(nombre_producto,))
la coma es que nos devuelve una tupla
NOTA: siempre cuando hacemos un delete, uptade, un insert nuestra conexion
termina en conexion.commiit() -> esto quiere decir que guardo los cambios

'''
# Eliminar un producto específico
nombre_producto="Lápiz"
cursor.execute('DELETE FROM productos WHERE nombre = ?',(nombre_producto,))


# Confirmar cambios
conexion.commit()


print(f"setencia DETELE ejecutada para '{nombre_producto}'.")



cursor.execute("SELECT * FROM productos WHERE nombre=?" ,(nombre_producto,))

todos_productos=cursor.fetchall() # aca guardamos el select




if not todos_productos:
    print(f"Los productos '{nombre_producto}' fue eliminado con existo")
   
else:
    for produc in todos_productos:
        print(f"ID: {produc[0]} NOMBRE: {produc[1]} PRECIO: {produc[2]:.2f}")


# Eliminar productos con precio menor a $50
# 1. Ver qué hay en la base de datos ANTES de hacer nada

cursor.execute("SELECT * FROM productos")
print("=== PRODUCTOS ANTES DEL DELETE ===")
antes_productos= cursor.fetchall()
for p in antes_productos:
    print(f"ID: {p[0]} | NOMBRE: {p[1]} | PRECIO: ${p[2]:.2f}")


precio_limite=50
cursor.execute("DELETE FROM productos WHERE precio < ?",(precio_limite,))

# GUARDAMOS cuántas filas se borraron ANTES de hacer el commit
filas_borradas = cursor.rowcount
print("\n=== VERIFICACIÓN DEL DELETE ===")
if filas_borradas == 0:
    # Si la base de datos nos dice que borró 0 filas...
    print(f"No se eliminó nada porque no existían productos con precio menor a ${precio_limite}.")
else:
    # Si borró 1 o más filas...
    print(f"¡Éxito! Se eliminaron correctamente {filas_borradas} productos menores a ${precio_limite}.")



# 3. Ver qué quedó en la base de datos DESPUÉS del DELETE
cursor.execute("SELECT * FROM productos")
print("\n=== PRODUCTOS QUE QUEDARON EN LA BASE DE DATOS ===")
productos_restantes = cursor.fetchall()

for p in productos_restantes:
    print(f"ID: {p[0]} | NOMBRE: {p[1]} | PRECIO: ${p[2]:.2f}")


# Cerrar la conexión

conexion.commit()
cursor.close()
conexion.close()
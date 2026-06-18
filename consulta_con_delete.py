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

precio_limite=50
cursor.execute("DELETE FROM productos WHERE precio < ?",(precio_limite))











# Cerrar la conexión
cursor.close()
conexion.close()
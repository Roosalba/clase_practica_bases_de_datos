from conexion_db import obtener_conexion

conexion=obtener_conexion()
cursor= conexion.cursor()



''' aca vamos actualizar los precios, para actualizar usamos el uptade
es uptade nombre_tabla set nombre_columna =? where condicion
la condicion es siempre el id, para usar el uptade se usa el where
porque sino se modifican todos los campos

'''
# Actualizar el precio de un producto egit pushspecífico
nuevo_precio=250.0
id=1

cursor.execute('UPDATE productos SET precio =? WHERE  id = ?',(nuevo_precio,id))

# confirmar cambios
conexion.commit()

print(f'Producto con ID {id} actualizado correctamente.')


#verificamos los cambios esto lo hacemos con el select
cursor.execute('SELECT * FROM productos WHERE id =?',(id,))

# esta es la variable que creamos para cuando se hace el select
producto_actualizado= cursor.fetchone()

print("\n=== Producto Actualizado ===")
if producto_actualizado is not None:
    print(f"ID:  {producto_actualizado[0]},  Nombre:  {producto_actualizado[1]}, Precio: ${producto_actualizado[2]:.2f}")
else:print(f"Error: El producto con ID {id} no existe en la base de datos.")


#  Incrementar en un 10% los precios de los productos con precio menor a
# $100

cursor.execute('UPDATE productos SET precio = precio * 1.10 WHERE precio < ? ',(100,))


# Confirmar cambios
conexion.commit()

print("Precios actualizados para productos con precio menor a $100.")
'''
siempre que se haga un update, delete, insert, la mejor practica es despues de hacerla
hacer un select para comprobar si los cambios se hicieron.

'''

cursor.execute('SELECT * FROM productos WHERE precio < ?',(100,))
productos_incrementados=cursor.fetchall()

print("los productos que fueron modificados son ")

for pro in productos_incrementados:
    print(f"ID: {pro[0]}, Nombre: {pro[1]}, Precio: {pro[2]:.2f}")

cursor.close()
conexion.close()


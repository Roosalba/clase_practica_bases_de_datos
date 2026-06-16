from conexion_db import obtener_conexion

conexion=obtener_conexion()
cursor= conexion.cursor()



''' aca vamos actualizar los precios, para actualizar usamos el uptade
es uptade nombre_tabla set nombre_columna =? where condicion
la condicion es siempre el id, para usar el uptade se usa el where
porque sino se modifican todos los campos

'''
# Actualizar el precio de un producto específico
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
print(f"ID:  {producto_actualizado[0]},  Nombre:  {producto_actualizado[1]}, Precio: ${producto_actualizado[2]:.2f}")







conexion.close()
from conexion_db import obtener_conexion




conexion=obtener_conexion()
cursor= conexion.cursor()
print("conexion con exito")


conexion.commit()
conexion.close()
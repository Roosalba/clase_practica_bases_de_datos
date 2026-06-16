import sqlite3

def obtener_conexion():
    conexion = sqlite3.connect("productos.db")
    return conexion



'''
cuando importe esto, despues tengo que colocarle al archivo esta parte
# Crear un objeto cursor
conexion=obtener_conexion()
cursor = conexion.cursor()

'''
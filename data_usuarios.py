from negocio import procesar_usuario
from datos import listado_usuarios
import os

def escribir_data_usuarios():
    lista_modificada = procesar_usuario()

    ruta_archivo = os.path.join('modulos/datos/data_almacenada','info_usuarios.py')
    ruta_absoluta = os.path.abspath(ruta_archivo)
    ruta_final = os.path.realpath(ruta_absoluta)
    archivo_libros = open(ruta_final,'+w', encoding="utf-8")
    archivo_libros.write(f'listado_usuarios = {lista_modificada}')
    archivo_libros.close()
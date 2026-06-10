from negocio.negocio_libros import procesar_libro
from datos import listado_libros
import os

def escribir_data_libros():
    lista_modificada = procesar_libro()

    ruta_archivo = os.path.join('modulos/datos/data_almacenada','info_libros.py')
    ruta_absoluta = os.path.abspath(ruta_archivo)
    ruta_final = os.path.realpath(ruta_absoluta)
    archivo_libros = open(ruta_final,'+w', encoding="utf-8")
    archivo_libros.write(f'listado_libros = {lista_modificada}')
    archivo_libros.close()
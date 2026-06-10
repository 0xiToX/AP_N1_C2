from presentacion.solicitud_datos import solicitar_datos_libro
from datos import listado_libros
from prettytable import PrettyTable

def procesar_libro():
    titulo_libro, isbn, editorial, paginas, categoria = solicitar_datos_libro()
    nuevo_libro = {
        'id': len(listado_libros) + 1,
        'titulo_libro':titulo_libro.title(),
        'isbn':isbn,
        'editorial':editorial,
        'paginas':paginas,
        'categoria':categoria.title()
    }
    listado_libros.append(nuevo_libro)
    return listado_libros

def crear_tabla_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['N°','Título','ISBN','Editorial','Páginas','Categoría']

    for libro in listado_libros:
        tabla_libros.add_row([libro['id'],libro['titulo_libro'],libro['isbn'],libro['editorial'],libro['paginas'],libro['categoria']])
    
    return tabla_libros

def buscar_libro(titulo):
    for libro in listado_libros:
        if libro['titulo_libro'].lower() == titulo.lower():
            return libro
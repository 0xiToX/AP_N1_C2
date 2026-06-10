import importlib
from datos import listado_libros


def test_imports_presentacion_menu():
    m = importlib.import_module('presentacion.menu_principal')
    assert hasattr(m, 'menu_principal')


def test_imports_negocio():
    m = importlib.import_module('negocio.negocio_libros')
    assert hasattr(m, 'crear_tabla_libros')
    assert hasattr(m, 'buscar_libro')


def test_buscar_libro_existente():
    m = importlib.import_module('negocio.negocio_libros')
    libro = m.buscar_libro('El Hobbit')
    assert libro is not None
    assert libro['titulo_libro'].lower() == 'el hobbit'


def test_crear_tabla_libros_retun_prettytable():
    m = importlib.import_module('negocio.negocio_libros')
    tabla = m.crear_tabla_libros()
    # PrettyTable prints to string; ensure header present
    s = str(tabla)
    assert 'Título' in s or 'Título' in repr(tabla)

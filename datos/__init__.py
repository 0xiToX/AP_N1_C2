import os
import sys

# Allow importing existing top-level modules from the project root
_pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if _pkg_root not in sys.path:
    sys.path.insert(0, _pkg_root)

# Re-export data modules so existing imports like "from datos import listado_libros" work
try:
    from data_almacenada.info_libros import listado_libros
except Exception:
    listado_libros = []

try:
    from data_almacenada.info_usuarios import listado_usuarios
except Exception:
    listado_usuarios = []

# Menus / version (optional)
try:
    from data_almacenada.info_menus import datos_menu, opciones_validas_menu, datos_sub_menu, mensaje_volver, opciones_validas_sub_menu, mensaje_opcion_incorrecta, titulo_app
except Exception:
    pass

try:
    from data_almacenada.info_version import numero_version
except Exception:
    numero_version = None

# Functions for writing data
try:
    from data_libros import escribir_data_libros
except Exception:
    def escribir_data_libros():
        raise RuntimeError('escribir_data_libros no disponible')

try:
    from data_usuarios import escribir_data_usuarios
except Exception:
    def escribir_data_usuarios():
        raise RuntimeError('escribir_data_usuarios no disponible')

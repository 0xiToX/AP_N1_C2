# Proyecto : Proyecto Modular
# Autor: Erick Bailey

"""
Un método de versionamiento del codigo es usar:
Version MAYOR.MENOR.PARCHE (Major, Minor, Patch)

MAJOR: Se incrementa cuando se hacen cambios grandes o
    incompatibles con version anterior, p.e.: cambio a base de datos, 
    integracion de nuevas funciones/capacidades, cambio de paradigma,
    cambio de arquitectura, etc.
MINOR: Se incrementa cuando se agregan funcionalidades nuevas
    pero sin romper la compatibilidad
PATCH: Se incrementa cuando se corrigen errores o se hacen 
    mejoras. p.e.: Agregan validaciones a la lectura de datos.
"""

# Historial
#   19.25.2026  : Inicio del proyecto (v1.0.0) Definir arquitectura en capas del proyecto (datos, negocio, presentacion). v1.0.0
#   20.05.2026  : Modificar menús de acceso a la aplicación. v1.0.1
#   26.05.2026  : Agregando funcionalidad para gestionar libros. v1.1.1
#   03.06.2026  : Creando métodos para crear, listar y modificar libros. v1.2.1

numero_version = '1.2.1'
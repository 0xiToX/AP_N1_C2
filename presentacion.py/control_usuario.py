from datos import listado_usuarios,escribir_data_usuarios
from prettytable import PrettyTable
from negocio import procesar_usuario,crear_tabla_usuarios,buscar_usuario
from presentacion.solicitud_datos import solicitar_dato,nuevos_datos_usuario

def agregar_usuario():
    titulo = '\nAgregar Usuario'
    print(titulo)
    print('=' * len(titulo))
    listar_usuarios()

    print('\nIngrese los datos del usuario:')
    escribir_data_usuarios()

def listar_usuarios():
    tabla_usuarios = PrettyTable()

    titulo = '\nListado de Usuarios'
    print(titulo)
    print('=' * len(titulo))
    tabla_usuarios = crear_tabla_usuarios()
    print(tabla_usuarios)

def modificar_usuario():
    titulo = '\nModificar Usuario'
    print(titulo)
    print('=' * len(titulo))
    nombre_usuario = solicitar_dato('Ingrese el nombre del usuario: ')
    usuario = buscar_usuario(nombre_usuario)
    print(f'\nDatos del Usuario\n{"=" * 17}')
    print(f'N°: {usuario['id']} \nNombre: {usuario['nombre']} \nEmail: {usuario['correo']} \nRUT: {usuario['rut']}')
    nuevos_datos_usuario()

def eliminar_usuario():
    titulo = '\nEliminar Usuario'
    print(titulo)
    print('=' * len(titulo))
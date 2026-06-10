from presentacion.solicitud_datos import solicitar_datos_usuario
from datos import listado_usuarios
from prettytable import PrettyTable

def procesar_usuario():
    nombre, correo, telefono, rut, contrasena = solicitar_datos_usuario()
    nuevo_usuario = {
        'id': len(listado_usuarios) + 1,
        'nombre':nombre.title(),
        'correo':correo,
        'telefono':telefono,
        'rut':rut,
        'contrasena':contrasena
    }
    listado_usuarios.append(nuevo_usuario)
    return listado_usuarios

def crear_tabla_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['N°','Nombre','Email','Celular','RUT']

    for usuario in listado_usuarios:
        tabla_usuarios.add_row([usuario['id'],usuario['nombre'],usuario['correo'],usuario['telefono'],usuario['rut']])
    
    return tabla_usuarios

def buscar_usuario(nombre):
    for usuario in listado_usuarios:
        if usuario['nombre'].lower() == nombre.lower():
            return usuario
import maskpass

def solicitar_datos_libro():
    titulo_libro = isbn = editorial = paginas = categoria = ''
    while titulo_libro == '':
        titulo_libro = input('Título: ').strip()
    while isbn == '':
        isbn = input('ISBN: ').strip()
    while editorial == '':
        editorial = input('Editorial: ').strip()
    while paginas == '':
        paginas = input('Cantidad de Páginas: ').strip()
    while categoria == '':
        categoria = input('Categoría: ').strip()
    return titulo_libro,isbn,editorial,paginas,categoria

def solicitar_datos_usuario():
    nombre_usuario = correo_usuario = telefono_usuario = rut_usuario = contrasena_usuario = ''
    while nombre_usuario == '':
        nombre_usuario = input('Nombre Usuario: ').strip()
    while correo_usuario == '':
        correo_usuario = input('Correo Electrónico: ').strip()
    while telefono_usuario == '':
        telefono_usuario = input('Teléfono: ').strip()
    while rut_usuario == '':
        rut_usuario = input('RUT: ').strip()
    while contrasena_usuario == '':
        contrasena_usuario = maskpass.askpass(prompt="Contraseña: ", mask="*").strip()
    return nombre_usuario,correo_usuario,telefono_usuario,rut_usuario,contrasena_usuario

def solicitar_dato(mensaje_input):
    tipo_dato = ''
    while tipo_dato == '':
        tipo_dato = input(f'{mensaje_input}').strip()
        return tipo_dato

def nuevos_datos_libro():
    pass

def nuevos_datos_usuario():
    pass
nombre_personal = 'erick bailey'
titulo_personal = 'Desarrollador .Net Fullstack'
ciudad = 'TEMUCO'
cadena_texto_vacia = ''
cadena_texto_numeros = '123456'
rut_personal = '12824290-2'
rut_completo = '128242902'

texto_multiple_lineas = '''Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. Cras eget diam purus. 
Phasellus interdum velit quis massa tempor, 
at aliquet arcu congue. Mauris eu nisl eget leo finibus volutpat. 
Donec commodo sed leo quis molestie. Phasellus in placerat velit. 
Nam vel lorem quis lorem tempus fringilla eget vitae ligula. 
Interdum et malesuada fames ac ante ipsum primis in faucibus. 
Nunc eget vestibulum tellus, eget semper odio. Aliquam at varius felis. 
Vestibulum sagittis mauris tristique, tempor magna vel, egestas mauris. 
Curabitur vestibulum euismod dolor at pulvinar. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra,
 per inceptos himenaeos.'''

# El método DIR, nos indica todos los métodos disponibles para la variable
print(dir(nombre_personal))

# Métodos de cadena, modifican el STRING asociado
# CAPITALIZE deja la primera letra de un string en mayúsculas
print(f'Su nombre personal CAPITALIZADO: {nombre_personal.capitalize()}')
# UPPER deja todo el STRING en mayúsculas
print(f'Su nombre personal MAYÚSCULAS: {nombre_personal.upper()}')
# TITLE deja la primera letra de cada palabra en mayúscula
print(f'Su nombre personal como TÍTULO: {nombre_personal.title()}')
# LOWER deja todo el STRING en minúsculas
print(f'Ciudad en MINÚSCULAS: {ciudad.lower()}')

# COUNT cuenta la cantidad de ocurrencias de un caracter
print(titulo_personal.count('e'))
# COUNT devuelve 0 si no encuentra el caracter buscado
print(titulo_personal.count('x'))

# FIND busca un SUBSTRING dentro de una cadena y devuelve el índice donde se encuentra
print(titulo_personal.find('llador'))
# FIND devuelve -1 si no encuentra el SUBSTRING
print(titulo_personal.find('x'))
# INDEX busca un SUBSTRING dentro de una cadena y devuelve el índice donde se encuentra
print(titulo_personal.index('llador'))
# INDEX devuelve ERROR si no encuentra el SUBSTRING, 
# porque no puede contar el índice de lo que no existe
# print(titulo_personal.index('x'))

# El método LEN permite conocer el TAMAÑO (length/largo) de los elementos
print(len(nombre_personal))
print(len(texto_multiple_lineas))

# Obteniendo SUBSTRING desde cadenas
titulo_personal_split = titulo_personal.split(' ');
print(titulo_personal_split)
print(type(titulo_personal_split))
print(titulo_personal_split[0])

titulo_personal_split_e = titulo_personal.split('e');
print(titulo_personal_split_e)

rut_split = rut_personal.split('-')
print(rut_split)
print(f'Rut: {rut_split[0]}')
print(f'Dígito Verificador: {rut_split[1]}')

rut_completo_split = rut_completo.split()[-1]
print(rut_completo_split[-1])
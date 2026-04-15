# Métodos para trabajar con listas

animales = ['Gato','Perro','Vaca','Conejo','Ornitorrinco','Murciélago']
frutas = ['Durazno','Fresa','Mango','Melón']
numeros = [5,6,7,1,56,789,2]

# El método APPEND agrega elementos al final de la lista
print(animales)
nuevo_animal = input('Agregue un nuevo animal a la lista: ')
animales.append(nuevo_animal.title())
print(animales)

print(len(animales))
# El método INSERT agrega un elemento en la posición indicada
otro_nuevo_animal = input('Agregue un nuevo animal a la lista: ')
animales.insert(0,otro_nuevo_animal.title())
print(animales)

# El método EXTEND permite agregar varios elementos a una lista
animales.extend(['Oveja','Cerdo'])
print(animales)
animales.extend(frutas)
print(animales)

# El método POP permite eliminar elementos de una lista
# POP sin argumentos elimina el último elemento de la lista
animales.pop()
print(animales)
# POP con el argumento ÍNDICE, elimina un elemento por su ubicación
animales.pop(2)
print(animales)
# El método REMOVE elimina un elemento por su valor
animales.remove('Vaca')
print(animales)

# Ordenando listas
# Si la lista es de STRINGS se ordena alfabéticamente
animales.sort()
print(animales)
# Si indicamos REVERSE = True, se ordena de forma alfabéticamente decreciente
animales.sort(reverse=True)
print(animales)

# Si la lista es de NÚMEROS se ordena de forma creciente
numeros.sort()
print(numeros)
# Si indicamos REVERSE = True, se ordena de forma decreciente
numeros.sort(reverse=True)
print(numeros)

# El método CLEAR limpia completamente la lista
animales.clear()
print(animales)
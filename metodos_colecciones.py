# Métodos para trabajar con listas 

animales = ['Gatos','Perros', 'Vaca', 'Conejo', 'Ornitorrinco', 'Murciélago']
frutas = ['Durazno', 'Fresa', 'Mango', 'Melon']


"El Método APPEND agrega elementos a la lista "
print(animales)
nuevo_animal = input('Agregue un nuevo animal a la lista')
animales.append(nuevo_animal)
print(animales)


print(len(animales))
#El Método INSERT agrega un elemento en la posición indicada 
otro_nuevo_animal = input('Agregue un nuevo animal a la lista')
animales.insert(0,otro_nuevo_animal)
print(animales)

animales.extend(['Oveja, Cerdo '])
print(animales) 
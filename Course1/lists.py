# Creación de listas
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]

print("Lista vacía:", lista_vacia)
print("Lista de números:", lista_numeros)
print("Lista mixta:", lista_mixta)

# Acceder a elementos
print("\nAcceso a elementos")
print("Primer elemento:", lista_numeros[0])
print("Último elemento:", lista_numeros[-1])

# Modificar elementos
print("\nModificar elementos")
lista_numeros[0] = 10
print("Lista de números modificada:", lista_numeros)

# Agregar y eliminar elementos
print("\nAgregar y eliminar elementos")
lista_numeros.append(6)
print("Lista después de append:", lista_numeros)
lista_numeros.insert(2, 99)
print("Lista después de insert:", lista_numeros)
lista_numeros.remove(99)
print("Lista después de remove:", lista_numeros)
ultimo = lista_numeros.pop()
print("Elemento eliminado con pop:", ultimo)
print("Lista después de pop:", lista_numeros)
elemento = lista_numeros.pop(1)
print("Elemento eliminado en la posición 1:", elemento)
print("Lista después de eliminar en la posición 1:", lista_numeros)

# Operaciones básicas
print("\nOperaciones básicas")
lista_concatenada = lista_numeros + lista_mixta
print("Lista concatenada:", lista_concatenada)
lista_repetida = lista_numeros * 2
print("Lista repetida:", lista_repetida)
print("¿Está 3 en la lista?", 3 in lista_numeros)
print("Longitud de la lista:", len(lista_numeros))

# Iteración sobre los elementos de una lista
print("\nIteración sobre elementos de la lista")
for elemento in lista_numeros:
    print(elemento)

# Salida final
print("\nGracias por utilizar el programa de listas. ¡Hasta la próxima!")

```# Creación de listas

lista\_vacia = \[]

lista\_numeros = \[1, 2, 3, 4, 5]

lista\_mixta = \[1, "dos", 3.0, True]



print("Lista vacía:", lista\_vacia)

print("Lista de números:", lista\_numeros)

print("Lista mixta:", lista\_mixta)



\# Acceder a elementos

print("\nAcceso a elementos")

print("Primer elemento:", lista\_numeros\[0])

print("Último elemento:", lista\_numeros\[-1])



\# Modificar elementos

print("\nModificar elementos")

lista\_numeros\[0] = 10

print("Lista de números modificada:", lista\_numeros)



\# Agregar y eliminar elementos

print("\nAgregar y eliminar elementos")

lista\_numeros.append(6)

print("Lista después de append:", lista\_numeros)

lista\_numeros.insert(2, 99)

print("Lista después de insert:", lista\_numeros)

lista\_numeros.remove(99)

print("Lista después de remove:", lista\_numeros)

ultimo = lista\_numeros.pop()

print("Elemento eliminado con pop:", ultimo)

print("Lista después de pop:", lista\_numeros)

elemento = lista\_numeros.pop(1)

print("Elemento eliminado en la posición 1:", elemento)

print("Lista después de eliminar en la posición 1:", lista\_numeros)



\# Operaciones básicas

print("\nOperaciones básicas")

lista\_concatenada = lista\_numeros + lista\_mixta

print("Lista concatenada:", lista\_concatenada)

lista\_repetida = lista\_numeros \* 2

print("Lista repetida:", lista\_repetida)

print("¿Está 3 en la lista?", 3 in lista\_numeros)

print("Longitud de la lista:", len(lista\_numeros))



\# Iteración sobre los elementos de una lista

print("\nIteración sobre elementos de la lista")

for elemento in lista\_numeros:

&#x20;   print(elemento)



\# Salida final

print("\nGracias por utilizar el programa de listas. ¡Hasta la próxima!")
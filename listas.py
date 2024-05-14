# 1. Crear una lista
lista= [1,2,3,4,5]
print(lista)

# 2. Imprimir un numero de la lista
print(lista[3])

# 3. Modificar el numero 1
lista[1]=10
print(lista)

# 4. Agregar un nuevo campo a la lista
lista.append(6)
print(lista)

# 5. Eliminar un elemento por valor
buscar=10
lista.remove(buscar)
print(lista)

# 6. Eliminar un elemento por indice
i=0
del lista[0]
print(lista)

# 7. Longitud de la lista
print(len(lista))

# 8. Extender la lista
lista.extend([7,8,9])
print(lista)

# 9. Insertar un elemento
lista.insert(0,0)
print(lista)

# 10. Limpiar la lista
lista.clear()
print(lista)

# 11. Revertir la lista
lista=[1,2,3,4,5]
lista.reverse()
print(lista)

# 12. Ordenar la lista
lista.sort()
print(lista)

# 13. Ordenar la lista en reversa
lista.sort(reverse=True)
print(lista)

# 14. Indice de un elemento
print(lista.index(4))
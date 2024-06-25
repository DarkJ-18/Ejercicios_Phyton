#2Modificar el tercer elemento de la lista para que sea el doble de su valor original y mostrar la lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[2]=lista[2]*2
print(lista)

#3Añadir el número 15 al final de la lista y mostrar la lista
lista.append(15)
print(lista)

#4 Crear una sublista con los tres primeros elementos de la lista y mostrar la sublista.
subLista = lista[:3]
print(subLista)


#5: Invertir el orden de los elementos en la lista y mostrarla
lista.reverse()
print(lista)

#6: Crear una nueva lista que contenga solo los elementos impares de la lista original y mostrarla.

listaImpares =[i for i in lista if i%2!=0]
print(listaImpares)

#7: Crear una lista con los cuadrados de los números del 1 al 5 y mostrar la lista.
lista2=[1,2,3,4,5]
listaCuadrados =[i**2 for i in lista2]
print(listaCuadrados)

#8: Comprobar si el número 8 está en la lista original y mostrar el resultado (True/False).
respuesta = False
if 8 in lista:
    respuesta=True
print(respuesta)    

#9: Crear una lista con los elementos de la lista original multiplicados por 3 y mostrar la lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaX3 = [i*3 for i in lista]
print(listaX3)

#10:Contar el número de elementos en la lista original que son mayores que 5 y mostrar el conteo.
conteo=len([ i for i in lista if i>5 ])
print(f"Hay {conteo} elementos mayores de 5 en la lista original")

#11:Crear una lista de las primeras cinco letras del alfabeto y agregar el conteo de > 5
listaAbecedario = ['a','b','c','d','e']
listaAbecedario.append(conteo)
print(listaAbecedario)

#12:Concatenar la lista de letras con la lista original y mostrar el resultado

listaAbecedario.append(lista)
print(listaAbecedario)

#13:Crear una lista que contenga la longitud de cada palabra en una lista de palabras dada y mostrar la lista de longitudes.
palabras = ["", "es", "genial"]
longitud =[len(indicePalabras) for indicePalabras in palabras]
print(longitud)

#14: Crear una lista con los números del 1 al 10 y eliminar el primer elemento que sea mayor que 5. Mostrar la lista resultante.

for i in lista:
    if i > 5:
        lista.remove(i)
        break
print(lista)

#15:Crear una lista con los elementos de la lista original elevados a la potencia de su índice y mostrar la lista.

potenciaIndice = [num ** i for i, num in enumerate(lista)]
print(potenciaIndice)

#16: Crear una lista con los primeros diez múltiplos de 3 y mostrar la lista.

listaMultiplos3 = [i for i in range(1,31) if i%3==0]
#listaMultiplos3 = [i*3 for i in range(1,11)]
print(listaMultiplos3)

#17:Crear una lista de las primeras cinco palabras de una lista de palabras y convertirlas a mayúsculas. Mostrar la lista resultante.
palabras = ["hola", "mundo", "", "es", "genial","Carro"]
palabrasMayus=[palabra.upper() for palabra in palabras[:5]]
print(palabrasMayus)

#18:Crear una lista de números del 1 al 10 y mostrar solo los números que no son múltiplos de 2.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaSinMultiplos2= [i for i in lista if i % 2 !=0]
print(listaSinMultiplos2)

#19:Crear una lista de palabras y mostrar solo las palabras que contienen la letra 'a'.
palabras = ["manzana", "pera", "melón", "kiwi", "naranja"]
palabrasA = [palabra for palabra in palabras if "a" in palabra]
print(palabrasA)

#20:Crear una lista con los elementos de la lista original ordenados en orden descendente y mostrar la lista.
lista.reverse()
print(lista)

#21:Crear una lista de listas donde cada sublista contenga tres números consecutivos, luego sumar los elementos de cada sublista y mostrar tanto las sublistas como sus sumas.
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Lista de listas:", lista_de_listas)
sumas = []
for sublista in lista_de_listas:
    suma_sublista = 0
    for num in sublista:
        suma_sublista += num
    sumas.append(suma_sublista)

print("Suma de los elementos de cada sublista:", sumas)
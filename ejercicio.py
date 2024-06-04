print("Bienvenido al Menu de Listas")

while True:
    x = int(input("Ingresa Numero:\n1--Sumar Lista\n2--Producto Lista\n3--Conteo 3\n4--Maximo y Minimo\n5--Sin Duplicados\n6--Cambio Posicion\n7--Invertir Sublista\n8--Pares e Impares\n9--Join\n10--Numero Mayor\n11--Suma Sublista\n12--Promedio\n13--Hallar Pares\n14--Al cuadrado\n15--Si existe?\n16--lista negativos\n17--Concatenar\n18--Pares tuplas\n19--Lista Primeros 5 Naturales\n20--Palabras Mayusculas\n21--Salir\nPara ejecutar: "))

    if x == 1:
        lista = [1, 2, 3, 4, 5]
        print(lista)
    elif x == 2:
        lista = [1, 2, 3, 4, 5]
        producto = 1
        for numero in lista:
            producto *= numero
        print(producto)
    elif x == 3:
        lista = [1, 2, 3, 4, 5, 3, 3]
        print(lista.count(3))
    elif x == 4:
        lista = [1, 2, 3, 4, 5]
        print(max(lista))
        print(min(lista))
    elif x == 5:
        lista = [1, 2, 3, 4, 5, 3, 3]
        print(list(set(lista)))
    elif x == 6:
        lista = [1, 2, 3, 4, 5]
        lista[0], lista[-1] = lista[-1], lista[0]
        print(lista)
    elif x == 7:
        lista = [1, 2, 3, 4, 5]
        sublista = lista[1:4][::-1]
        lista[1:4] = sublista
        print(sublista)
    elif x == 8:
        lista = [1, 2, 3, 4, 5]
        pares = sum(1 for num in lista if num % 2 == 0)
        impares = sum(1 for num in lista if num % 2 != 0)
        print(pares)
        print(impares)
    elif x == 9:
        frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
        print("".join(frutas))
    elif x == 10:
        lista = [1, 2, 3, 4, 5]
        print([num for num in lista if num > 3])
    elif x == 11:
        lista = [1, 2, 3, 4, 5]
        print(sum(lista[1:4]))
    elif x == 12:
        lista = [1, 2, 3, 4, 5]
        print(sum(lista) / len(lista))
    elif x == 13:
        lista = [1, 2, 3, 4, 5]
        print([num for num in lista if num % 2 == 0])
    elif x == 14:
        print([num**2 for num in range(1, 6)])
    elif x == 15:
        lista = [1, 2, 3, 4, 5]
        print(3 in lista)
    elif x == 16:
        print([-num for num in range(1, 11)])
    elif x == 17:
        lista1 = [1, 2, 3]
        lista2 = [4, 5, 6]
        print(lista1 + lista2)
    elif x == 18:
        lista1 = [1, 2, 3]
        lista2 = ["a", "b", "c"]
        print(list(zip(lista1, lista2)))
    elif x == 19:
        print(list(range(1, 6)))
    elif x == 20:
        palabras = ["HoLa", "MUNDO", "pYThon"]
        print([palabra.upper() for palabra in palabras])
    elif x == 21:
        print("Hasta Pronto :)")
        break
import os 
os.system("clear")

producto =[]
cantidad =[]
precio=[]

opc=0
while opc != 9:
    print("1-Crear un producto\n2--Buscar Un producto\n3--Actualizar Producton\n4--Eliminar producto\n5--Lista de productos\n6--Ordenar producto por nombre\n7--Invertir los productos\n8--Eliminar todos los productos\n9--Salir")
    opc=int(input("Ingrese su opcion: "))

    if opc ==1:
        os.system("clear")
        print("---Crear Producto---")
        nombreP = input("Ingresa el nombre del producto: ").capitalize()
        cantidadP = int(input("Ingrese cantidad del producto: "))
        precioP = float(input("Ingrese el precio del producto: "))

        producto.append(nombreP)
        cantidad.append(cantidadP)
        precio.append  (precioP)

        print("---Producto Agregado con exito---")

    elif opc ==2:
        os.system("clear")
        buscarProducto = input("Que producto deseas buscar?: ").capitalize()
        resultado = buscarProducto in producto

        if resultado == True:
            print("---Producto encontrado---")
            elemento = producto.index(buscarProducto)

            print("Nombre del producto ",producto[elemento])
            print("Cantidad del producto ",cantidad[elemento])
            print("Precio del producto ",precio[elemento])
        else:
                print("----- Producto No encontrado -----")


    elif opc ==3:
        os.system("clear")
        buscarProducto = input("Que producto deseas Actualizar?: ").capitalize()
        resultado = buscarProducto in producto

        if resultado == True:
            print("---Producto encontrado---")
            elemento = producto.index(buscarProducto)
            nuevoNombreP = input("Ingresa elnuevo nombre del producto: ").capitalize()
            nuevaCantidadP = int(input("Ingrese la nueva cantidad del producto: "))
            nuevoPrecioP = float(input("Ingrese el nuevo precio del producto: "))

            producto[elemento]= nuevoNombreP
            cantidad[elemento]= nuevaCantidadP
            precio[elemento]  = nuevoPrecioP
            
            print("----- Producto actualizado correctamente -----")
        else:
            print("----- Producto No encontrado -----") 

    elif opc ==4:
        os.system("clear")
        buscarProducto = input("Que producto deseas Eliminar?: ").capitalize()
        resultado = buscarProducto in producto

        if resultado == True:
            print("---Producto encontrado---")
            elemento = producto.index(buscarProducto)

            del producto[elemento]
            del cantidad[elemento]
            del precio[elemento]
            print("---Elemento eliminado con exito---")
        else:
            print("---El producto no fue encontrado---")    

    elif opc ==5:
        os.system("clear")
        if producto:
            print("---Lista de productos---")
            for p,c,pr in zip(producto,cantidad,precio):
                print(f"producto: {p} Cantidad: {c} Precio: {pr}")
        else:
            print("---No hay productos para mostrar---")
    elif opc ==6:
        os.system("clear")
        if producto:
            
            producto,cantidad,precio = zip(*sorted(zip[producto,cantidad,precio]))

            print("---Lista de productos en orden---")
            for p,c,pr in zip(producto,cantidad,precio):
                print(f"producto: {p} Cantidad: {c} Precio: {pr}")
        else:
            print("---No hay productos para mostrar---")

    elif opc ==7:
        os.system("clear")
        if producto:
            producto.reverse()
            cantidad.reverse()
            precio.reverse()
        else:
            print("---No hay productos para mostrar---")
    elif opc ==8:
        os.system("clear")
        if producto:
            producto.clear()
            cantidad.clear()
            precio.clear()

            

    elif opc ==9:
        os.system("clear")
        print("El perico no se vende aca!!")
        
#------------------------------

print("Bienvenido al Menu")

i = True

while i == True:

    x = int(input("Ingresa Numero:\n1--Sumar Lista\n2--Producto Lista\n3--Conteo 3\n4--Maximo y Minimo\n5--Sin Duplicados\n6--Cambio Posicion\n7--Invertir Sublista\n8--Pares e Impares\n9--Join\n10--Numero Mayor\n11--Suma Sublista\n12--Promedio\n13--Hallar Pares\n14--Al cuadrado\n15--Si existe?\n16--lista negativos\n17--Concatenar\n18--Pares tuplas\n19--Lista Primeros 5 Naturales\n20--Palabras Mayusculas\n21--Salir\nPara ejecutar: "))

    if x == 1:

        lista = [1, 2, 3, 4, 5]

        print(lista)

    elif x == 2:

        lista = [1, 2, 3, 4, 5]

        producto = 1
        for numero in lista:
            producto = producto * numero

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

        sublista = lista[1:4]

        sublista.reverse()

        lista[1:4] = sublista

        print(sublista)

    elif x == 8:

        lista = [1, 2, 3, 4, 5]

        pares = len([num for num in lista if num % 2 == 0])

        impares = len([num for num in lista if num % 2 != 0])

        print(pares)

        print (impares)

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

        lista2 = ['a', 'b', 'c']

        print(list(zip(lista1, lista2)))

    elif x == 19:

        print(list(range(1, 6)))

    elif x == 20:

        palabras = ["HoLa", "MUNDO", "pYThon"]

        print([palabra.upper() for palabra in palabras])

    elif x == 21:

        print("Hasta Pronto")

        i = False
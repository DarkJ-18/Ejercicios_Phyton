#22 Ejercicio práctico hacer un CRUD solo con las funciones append y del
#con la posición del elemento en el vector actualizo y busco, con append agrego y con del elimino 


print("Bienvenido al Sistema de Inventario")

producto = []
cantidad = []
precio = []


while True:
    try:
        
        opc = int(input("Ingresa una opcion\n 1. CREAR PRODUCTO \n 2. BUSCAR PRODUCTON\n 3. ACTUALIZAR PRODUCTO\n 4. ELIMINAR PRODUCTO\n 5.SALIR "))
        
        if opc == 1:
            print("CREANDO PRODUCTOS")
            product = input("Ingresa nombre del producto: ").capitalize()
            amount = input("Ingrese la cantidad del producto: ")
            price = float(input("ingrese el precio del producto: "))
            
            producto.append(product)
            cantidad.append(amount)
            precio.append(price)
            
            print("Producto registrado correctamente")
          
        elif opc == 2:
              searchProduct = input("Ingresa el producto a buscar: ").capitalize()
              result = searchProduct in producto
              
              if result == True
              
              
               
              
        
    except ValueError:
        print("Por favor ingrese un valor")
            
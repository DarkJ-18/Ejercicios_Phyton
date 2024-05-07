import os


try:
    
    mensaje=("Menu de opciones: Opc 1\n opc 2 \nopc 3 \n salir 4 ")
    menu=True
    while menu:
        print(mensaje)
        opcion=input("Ingrese una opcion: ")
        os.system('clear')
        if opcion=="1":
            print("Opcion 1")
        elif opcion=="2":
            print("Opcion 2")
        elif opcion=="3":
            print("Opcion 3")
        elif opcion=="4":
            print("Salir")
            menu=False
    print("fin")
except:
    print("Error")
            
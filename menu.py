import os
os.system('clear')

try:
    
    mensaje=("Menu de opciones: Opc 1 /opc 2 /opc 3 /salir 4 ")
    menu=True
    while menu:
       
        print(mensaje)
        os.system('clear')
        opcion=input("Ingrese una opcion: ")
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
            
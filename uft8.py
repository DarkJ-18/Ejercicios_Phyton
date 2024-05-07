import keyboard

def char_to_utf8(char): # convierte un caracter a su código UTF-8
    return ord(char) 

def utf8_to_char(utf8_code): # convierte un código UTF-8 a su caracter
    return chr(utf8_code) 

while True:
    try:
        entrada = input("Ingrese una tecla o un código UTF-8 ('q' para salir): ")
        
        if entrada == 'q':
            print("Saliendo del programa...")
            break
        
        if len(entrada) == 1: # si la entrada tiene longitud 1, es una tecla
            tecla = entrada
            codigo = char_to_utf8(tecla) # se convierte la tecla a su código UTF-8
            print(f"La tecla '{tecla}' tiene el código UTF-8: {codigo}")
        else:    
            codigo = int(entrada)  
            tecla = utf8_to_char(codigo) # se convierte el código UTF-8 a su tecla
            print(f"La tecla para el código UTF-8 {codigo} es: '{tecla}'") 
    except ValueError:
        print("Por favor ingrese una tecla valida")

#keyboard.wait('esc')


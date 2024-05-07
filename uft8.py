import keyboard

def char_to_utf8(char): 
    return ord(char) 

def utf8_to_char(utf8_code): 
    return chr(utf8_code) 

while True:
    try:
        entrada = input("Ingrese una tecla o un código UTF-8 ('esc' para salir): ")
        
        if entrada == 'esc': 
            print("Saliendo del programa...")
            break
        
        if len(entrada) == 1: # si la entrada tiene longitud 1, es una tecla
            tecla = entrada
            codigo = char_to_utf8(tecla) 
           
        
          


#keyboard.wait('esc')

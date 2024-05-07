import keyboard

# Funciones para convertir un carácter a su código UTF-8 y viceversa
def char_to_utf8(char):
    return ord(char)

def utf8_to_char(utf8_code):
    return chr(utf8_code)

# Función que se ejecutará cuando se presione una tecla
def on_key_pressed(event):
    key = event.name
    
    # Verifica si se presionó la tecla "x" para convertir un carácter a su código UTF-8
    if key == "x":
        char = input("Ingrese un carácter para obtener su código UTF-8: ")
        utf8_code = char_to_utf8(char)
        print(f"El código UTF-8 para '{char}' es: {utf8_code}")
    
    # Verifica si se presionó la tecla "c" para convertir un código UTF-8 a un carácter
    elif key == "c":
        utf8_code = int(input("Ingrese un código UTF-8 para obtener su carácter: "))
        char = utf8_to_char(utf8_code)
        print(f"El carácter para el código UTF-8 {utf8_code} es: '{char}'")

# Configura el detector de teclas
keyboard.on_press(on_key_pressed)

# Mantén el programa en ejecución para que pueda detectar las pulsaciones de teclas
keyboard.wait('esc')

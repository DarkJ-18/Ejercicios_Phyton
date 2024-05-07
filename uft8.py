import keyboard



def on_key_pressed(event): # funcion que se ejecuta cuando se presiona una tecla
   
    print("Tecla presionada:", event.name) # imprime la tecla presionada


keyboard.on_press(on_key_pressed) # llama a la funcion on_key_pressed cuando se presiona una tecla


keyboard.wait('esc') # espera a que se presione la tecla esc para terminar el programa

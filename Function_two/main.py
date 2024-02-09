from function_two import *

string = "Hola como te va"
character = "2"
new_character = "i"
new_string, number_replacements = replace_character(string, character, new_character)

if number_replacements != 0:
    print(f"A la cadena {string} se le reemplazo el carácter {character} por el carácter {new_character}")
    print(f"La nueva cadena es {new_string} hubo {number_replacements} reemplazos.")
else:
    print(new_string)
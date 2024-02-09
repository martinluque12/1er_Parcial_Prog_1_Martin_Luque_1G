from function_three import *

string = "zwbar"

sorted_string = sort_characters(string)

if sorted_string:
    print(f"La cadena a ordenar: {string}\nLa cadena ordenada: {sorted_string}")
else:
    print("¡Error! Parámetros no validos.")
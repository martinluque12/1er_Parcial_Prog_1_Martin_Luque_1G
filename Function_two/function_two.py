def replace_character(string: str, character: str, new_character: str) -> tuple:
    """Reemplaza un carácter en una cadena de texto por otro y cuenta las veces que se reemplazo.

    Args:
        string (str): La cadena de texto.
        character (str): El carácter a reemplazar.
        new_character (str): El nuevo carácter que se va a poner en lugar del anterior.

    Returns:
        tuple:  Una tupla con dos valores. En el primer valor está la cadena original
                y en segundo lugar la cantidad de veces que se reemplazo el carácter.
    """
    if(isinstance(string, str) and isinstance(character, str) and
       isinstance(new_character, str) and character in string):
        
        number_replacements = string.count(character)
        new_string = string.replace(character, new_character)

        return new_string, number_replacements
    else:
        return "Los parámetros no son válidos", 0
    

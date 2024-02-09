def sort_characters(string: str) -> str:
    """Ordena una cadena de texto de la A a la Z.

    Args:
        string (str): La cadena a ordenar.

    Returns:
        str: La cadena ordenada o un string vacío.
    """
    if isinstance(string, str):

        character = list(string)
        list_size = len(character)
        
        for i in range(0, list_size -1):
            for j in range(i + 1, list_size):
                if character[i] > character[j]:
                    character[i], character[j] = character[j], character[i]
        
        sorted_string = "".join(character)

        return sorted_string
    else:
        return ""
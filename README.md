<div align="center">
  <h1>Funciones para Manipulación de Cadenas y Precios</h1>
</div>
<div>
  <h2>Este repositorio contiene tres funciones en Python diseñadas para realizar operaciones comunes en cadenas de texto y manipulación de precios.</h2>
</div>

<h2>Funciones</h2>

* apply_increase()

Esta función permite aplicar un aumento del 5% a un precio dado.

def apply_increase(price_product: float) -> float:

      """
      Aplica un aumento del 5% a un precio.
      
      Args:
          price_product (float): El precio al cual se le aplicará el aumento.
      
      Returns:
          float: El precio más el aumento del 5%.
      
      """

* replace_character()

Esta función reemplaza un carácter en una cadena de texto por otro y cuenta las veces que se realizó el reemplazo.

def replace_character(string: str, character: str, new_character: str) -> tuple:

  """
  Reemplaza un carácter en una cadena de texto por otro y cuenta las veces que se reemplazó.
  
  Args:
      string (str): La cadena de texto.
      character (str): El carácter a reemplazar.
      new_character (str): El nuevo carácter que se pondrá en lugar del anterior.
  
  Returns:
      tuple: Una tupla con dos valores. En el primer valor está la cadena original
             y en segundo lugar la cantidad de veces que se reemplazó el carácter.
  
  """



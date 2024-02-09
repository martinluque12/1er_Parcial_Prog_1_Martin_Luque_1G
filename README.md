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
      """Aplica un aumento del 5% a un precio.
      
      Args:
          price_product (float): El precio al cual se le aplicará el aumento.
      
      Returns:
          float: El precio más el aumento del 5%.
      """

* replace_character()

Esta función reemplaza un carácter en una cadena de texto por otro y cuenta las veces que se realizó el reemplazo.

    def replace_character(string: str, character: str, new_character: str) -> tuple:
      """Reemplaza un carácter en una cadena de texto por otro y cuenta las veces que se reemplazó.
      
      Args:
          string (str): La cadena de texto.
          character (str): El carácter a reemplazar.
          new_character (str): El nuevo carácter que se pondrá en lugar del anterior.
      
      Returns:
          tuple: Una tupla con dos valores. En el primer valor está la cadena original
                 y en segundo lugar la cantidad de veces que se reemplazó el carácter.
      """

* sort_characters()

Esta función ordena una cadena de texto de la A a la Z.

    def sort_characters(string: str) -> str:
      """Ordena una cadena de texto de la A a la Z.
  
      Args:
          string (str): La cadena a ordenar.
  
      Returns:
          str: La cadena ordenada o un string vacío si no se proporciona una cadena válida.
      """

<h2>📔Uso:📔 </h2>
Para utilizar las funciones en tu código Python, debes importarlas desde las respectivas carpetas correspondientes. Aquí tienes cómo hacerlo para cada una de las funciones:

### 1. `apply_increase()`

Para importar la función `apply_increase()` desde `Function_one`, puedes hacerlo de la siguiente manera en tu código Python:

```python
from Function_one.function_one import apply_increase.
```

### 2. `replace_character()`

Para importar la función `replace_character()` desde `Function_two`, puedes hacerlo de la siguiente manera en tu código Python:

```python
from Function_two.function_two import replace_character
```

### 3. `sort_characters()`

Para importar la función `sort_characters()` desde `Function_three`, puedes hacerlo de la siguiente manera en tu código Python:

```python
from Function_three.function_three import sort_characters
```


Una vez que hayas importado las funciones correctamente, podrás utilizarlas según sea necesario en tu programa.

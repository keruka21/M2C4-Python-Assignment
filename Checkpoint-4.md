## Preguntas M2C4 

**¿Cuál es la diferencia entre una lista y una tupla en Python?**

Ambos son data types que contienen una lista de elementos ordenados.

Su principal diferencia es que las listas son mutables y se representan con los elementos entre corchetes [] mientras que las tuplas son inmutables y sus elementos se representan entre paréntesis ().


Ejemplos de tuplas:
```python
tupla_integrales = (1, 2, 3)
tupla_texto = ('a', 'b', 'c')
tupla_booleana = (True, False)
```
*No se puede editar ni el orden ni el contenido*

Ejemplos de listas:
```python
lista_integrales = [1, 2, 3, 4, 5]
lista_texto = ['a', 'b', 'c', 'd', 'e']
lista_booleana = [True, False, True]
```
*El contenido y su orden es editable*

**¿Cuál es el orden de las operaciones?**

El orden de las operaciones en Python es igual al orden jerárquico de las operaciones aritméticas.

Primero se realizarian las operaciones dentro de los paréntesis, luego las operaciones de exponentes, las de multiplicación y división y por último las de suma y resta.

Ejemplo:
```python
resultado_operacion = (1 + 2) ** 2 / 3 - (4 * 5)
print(resultado_operacion) #-17.0
```
*(3) ** 2 / 3 - (20)* 
*9/3-20*
*3.0-20*
*-17.0*

**¿Qué es un diccionario Python?**

Un diccionario es un data type que almacena datos en parejas compuestas por una clave y su valor.
La sintáxis básica seria {clave: valor, clave: valor, clave: valor}

Ejemplo:
```python
mi_diccionario = {
    "valor1": 21,
    "valor2": 42
}
primer_numero = mi_diccionario["valor1"] #los valores estan indexados gracias a sus claves
print(primer_numero) #21
```

**¿Cuál es la diferencia entre el método ordenado y la función de ordenación?**

El método sorted() nos devuelve ordenados los elementos de una lista pero sin modificar el orden original de la lista.
```python
mi_lista = [5, 1, 3, 2, 4]
mi_lista_ordenada = sorted(mi_lista)
print(mi_lista) #[5, 1, 3, 2, 4]
print(mi_lista_ordenada) #[1, 2, 3, 4, 5]
```
*La lista "mi_lista" no cambia*

El método sort() reorganizaria los elementos de la lista pero cambiando el orden original de la lista.
```python
mi_lista = [5, 1, 3, 2, 4]
mi_lista.sort()
print(mi_lista) #[1, 2, 3, 4, 5]
```
*La lista cambia*

**¿Qué es un operador de reasignación?**

Es el símbolo "=" que realiza la operación de asignar un valor a una variable. En el caso de que queramos reasignar un valor a una variable ya establecida también usariamos "="
```python
mi_variable = 21 #21 seria el valor de la variable mi_variable
mi_variable = 12 #ahora mi_variable tendria el valor de 12
```

## Ejercicios M2C4 Python Assignment

**Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.**

```python
mi_lista = ["a", "b", "c"]
mi_tupla = (1, 2, 3,)
mi_float = 21.212121
mi_entero = 42
mi_decimal = 1.5
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
```

**Exercise 2: Round your float up.**

```python
mi_float = 21.212121
float_redondeado = round(mi_float)
print(float_redondeado) #21
```

**Exercise 3: Get the square root of your float.**

```python
import math
mi_float = 21.212121
raiz_cuadrada = math.sqrt(mi_float)
print(raiz_cuadrada) #4.605661841690074
```

**Exercise 4: Select the first element from your dictionary.**

```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
primer_elemento = mi_diccionario['a']
print(primer_elemento) #1
```

**Exercise 5: Select the second element from your tuple.**

```python
mi_tupla = (1, 2, 3,)
segundo_elemento_tupla = mi_tupla[1]
print(segundo_elemento_tupla) #2
```
*El index del segundo elemento es 1.*

**Exercise 6: Add an element to the end of your list.**

```python
mi_lista = ["a", "b", "c"]
mi_lista.append("d")
print(mi_lista) #["a", "b", "c", "d"]
```
*Con la función .append podemos añadir un elemento al final de una lista.*

**Exercise 7: Replace the first element in your list.**

```python
mi_lista = ["a", "b", "c"]
mi_lista[0] = 21
print(mi_lista) #mi_lista = [21, "b", "c"]
```
*Reasignamos el valor del primer elemento (index 0) de una lista con =*

**Exercise 8: Sort your list alphabetically.**

```python
mi_lista = ["c", "a", "d", "b"]
mi_lista.sort()
print(mi_lista) #["a", "b", "c", "d"]
```
*La función .sort() sin argumento ordenará la lista alfabéticamente en caso de que sea una lista compuesta por elementos de texto, en caso de que fueran elementos numéricos por ejemplo integrales los colocaria de menor a mayor*

**Exercise 9: Use reassignment to add an element to your tuple.**

```python
mi_tupla = (1, 12, 42)
mi_tupla = mi_tupla + (21,)
print(mi_tupla) #(1, 12, 42, 21)
```

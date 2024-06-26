

#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.**

mi_lista = ["a", "b", "c"]
mi_tupla = (1, 2, 3,)
mi_float = 21.212121
mi_entero = 42

from decimal import Decimal
mi_decimal = Decimal('1.5')
print(mi_decimal)

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}



#Exercise 2: Round your float up.

import math

mi_float = 21.212121
mi_float_redondeado = math.ceil(mi_float)
print(float_redondeado)  #22



#Exercise 3: Get the square root of your float.

import math
mi_float = 21.212121
raiz_cuadrada = math.sqrt(mi_float)
print(raiz_cuadrada) #4.605661841690074



#Exercise 4: Select the first element from your dictionary.

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
primer_elemento = mi_diccionario['a']
print(primer_elemento) #1



#Exercise 5: Select the second element from your tuple.

mi_tupla = (1, 2, 3,)
segundo_elemento_tupla = mi_tupla[1]
print(segundo_elemento_tupla) #2 
#El index del segundo elemento es 1.



#Exercise 6: Add an element to the end of your list. 

mi_lista = ["a", "b", "c"]
mi_lista.append("d")
print(mi_lista) #["a", "b", "c", "d"] 
#Con la función .append podemos añadir un elemento al final de una lista.



#Exercise 7: Replace the first element in your list.

mi_lista = ["a", "b", "c"]
mi_lista[0] = 21
print(mi_lista) #mi_lista = [21, "b", "c"] 
#Reasignamos el valor del primer elemento (index 0) de una lista con =



#Exercise 8: Sort your list alphabetically.

mi_lista = ["c", "a", "d", "b"]
mi_lista.sort()
print(mi_lista) #["a", "b", "c", "d"]
#La función .sort() sin argumento ordenará la lista alfabéticamente en caso de que sea una lista compuesta por elementos de texto, en caso de que fueran elementos numéricos por ejemplo integrales los colocaria de menor a mayor



#Exercise 9: Use reassignment to add an element to your tuple.

mi_tupla = (1, 12, 42)
mi_tupla += (21,)
print(mi_tupla) #(1, 12, 42, 21)


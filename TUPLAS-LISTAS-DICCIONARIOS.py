# Definición de una lista en Python
lista = [1, 2, 3, "cuatro", "cinco"]
# Una lista es una colección ordenada y mutable de elementos, que pueden ser de diferentes tipos de datos.

# Accediendo a elementos de una lista
print("El primer elemento de la lista es:", lista[0])
print("El tercer elemento de la lista es:", lista[2])
print("El último elemento de la lista es:", lista[-1])
# Los elementos de una lista pueden ser accedidos utilizando su índice. El primer elemento tiene índice 0, y el último -1.

# Modificando elementos de una lista
lista[0] = "uno"
print("La lista modificada es:", lista)
# Los elementos de una lista pueden ser modificados, ya que las listas son mutables.

# Definición de una tupla en Python
tupla = (1, 2, 3, "cuatro", "cinco")
# Una tupla es una colección ordenada e inmutable de elementos, que pueden ser de diferentes tipos de datos.

# Accediendo a elementos de una tupla
print("El primer elemento de la tupla es:", tupla[0])
print("El tercer elemento de la tupla es:", tupla[2])
print("El último elemento de la tupla es:", tupla[-1])
# Los elementos de una tupla pueden ser accedidos utilizando su índice, al igual que en las listas.

# Intentando modificar elementos de una tupla (esto dará error)
tupla[0] = "uno"
# Los elementos de una tupla no pueden ser modificados, ya que las tuplas son inmutables.

# Definición de un diccionario en Python
diccionario = {"nombre": "Juan", "edad": 25, "pais": "México"}
# Un diccionario es una colección no ordenada de elementos, que son almacenados en pares clave-valor. Los diccionarios son mutables.

# Accediendo a elementos de un diccionario
print("El valor de la clave 'nombre' es:", diccionario["nombre"])
print("El valor de la clave 'edad' es:", diccionario["edad"])
print("El valor de la clave 'pais' es:", diccionario["pais"])
# Los elementos de un diccionario pueden ser accedidos utilizando su clave.

# Modificando elementos de un diccionario
diccionario["edad"] = 26
print("El diccionario modificado es:", diccionario)
# Los elementos de un diccionario pueden ser modificados, ya que los diccionarios son mutables.

# Añadiendo nuevos elementos a un diccionario
diccionario["profesion"] = "Programador"
print("El diccionario con un nuevo elemento es:", diccionario)
# Nuevos elementos pueden ser añadidos a un diccionario simplemente asignándoles una nueva clave y valor.

# Eliminando elementos de un diccionario
del diccionario["edad"]
print("El diccionario sin el elemento 'edad' es:", diccionario)
# Elementos de un diccionario pueden ser eliminados utilizando la instrucción 'del'.

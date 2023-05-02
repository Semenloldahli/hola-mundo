mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}

mi_diccionario = dict([("nombre", "Juan"), ("edad", 30), ("ciudad", "Buenos Aires")])

print(mi_diccionario["nombre"])  # Imprime "Juan"
print(mi_diccionario["edad"])  # Imprime 30

print(mi_diccionario.get("nombre", "No hay información"))  # Imprime "Juan"
print(mi_diccionario.get("altura", "No hay información"))  # Imprime "No hay información"

mi_diccionario["telefono"] = "555-1234"  # Agrega un nuevo elemento al diccionario
mi_diccionario["edad"] = 31  # Modifica el valor de un elemento existente

del mi_diccionario["ciudad"]  # Elimina el elemento con clave "ciudad"

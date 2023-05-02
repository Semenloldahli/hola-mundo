


mi_lista = []  # Creamos una lista vacía

while True:  # Ciclo infinito hasta que el usuario decida salir
    entrada = input("Ingresa un elemento para agregar a la lista (o escribe 'salir' para terminar): ")
    
    if entrada == "salir":
        break  # Salimos del ciclo si el usuario escribe 'salir'
    
    mi_lista.append(entrada)  # Agregamos el elemento a la lista

print("La lista resultante es:", mi_lista)  # Imprimimos la lista completa

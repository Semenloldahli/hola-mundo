# Pedir al usuario el ancho y la altura del rectángulo
ancho = float(input("Introduce el ancho del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

# Calcular el área y el perímetro del rectángulo
area = ancho * altura
perimetro = 2 * (ancho + altura)

# Mostrar el resultado
print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)
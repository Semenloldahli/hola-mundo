# Operadores aritméticos
num1 = 10
num2 = 5
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2
exponente = num1 ** num2
division_entera = num1 // num2

print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)
print("El módulo es:", modulo)
print("El exponente es:", exponente)
print("La división entera es:", division_entera)

# Operadores de comparación
a = 5
b = 10
print("a es igual a b?", a == b)
print("a es diferente de b?", a != b)
print("a es mayor que b?", a > b)
print("a es menor que b?", a < b)
print("a es mayor o igual que b?", a >= b)
print("a es menor o igual que b?", a <= b)

# Operadores lógicos
x = True
y = False
print("x and y es:", x and y)
print("x or y es:", x or y)
print("not x es:", not x)

# Operadores de identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print("lista1 es la misma que lista2?", lista1 is lista2)
print("lista1 es diferente de lista2?", lista1 is not lista2)
print("lista1 es la misma que lista3?", lista1 is lista3)

# Operadores de pertenencia
frutas = ["manzana", "naranja", "banana"]
print("manzana está en la lista de frutas?", "manzana" in frutas)
print("pera no está en la lista de frutas?", "pera" not in frutas)

# Operadores bitwise
a = 60 # 0011 1100
b = 13 # 0000 1101
c = a & b # 0000 1100
d = a | b # 0011 1101
e = a ^ b # 0011 0001
f = ~a # 1100 0011
g = a << 2 # 1111 0000
h = a >> 2 # 0000 1111

print("El resultado de a & b es:", c)
print("El resultado de a | b es:", d)
print("El resultado de a ^ b es:", e)
print("El resultado de ~a es:", f)
print("El resultado de a << 2 es:", g)
print("El resultado de a >> 2 es:", h)

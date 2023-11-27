Name = "KARINA"
print(Name)
a = 5
b = 10
print(a + b)
base = 10
altura = 5
area = (base * altura) / 2
print(area)
print(17 % 3)
numero = 12
if numero > 0:
    print("Positivo")
else:
    print("Negativo")
numero = 12
if numero % 2 == 0:
    print("par")
else:
    print("impar")
a = 1
b = 3
c = 5
mayor = max(a, b, c)
print(mayor)
for i in range(1, 11):
    print(i)
while a <= 20:
    if a % 2 == 0:
        print(a)
    a += 1
suma = 0
for i in range(1, 101):
    suma += i
print(suma)


def suma(a, b):
    return a + b


print(suma(8, 12))


#  Define una función que tome un número y retorne su factorial.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))


#  Define una función que tome un número y retorne su factorial.
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(es_primo(10))


# Define una función que reciba una lista de números y retorne la suma de ellos
def sumar_lista(lista):
    return sum(lista)


print(sumar_lista([1, 5, 4, 6, 9, 100]))


# Defina una función que reciba una cadena de texto y retorne la cadena en reversa
def reversa(cadena):
    return cadena[::-1]


print(reversa("Karina"))


# Crea una función para verificar si un número es par o impar y devuelve "El número es par" o "El numero es impar" según corresponda


def es_par(numero):
    return numero % 2 == 0


if es_par(9):
    print("Es un numero par.")
else:
    print("Es un numero impar.")


# Crea una funcion a la que pases numeros como argumento, calcule el factorial de ese número y haga print del resultado
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return


num = int(input("3"))
print("El factorial de 3 es:", factorial(3))

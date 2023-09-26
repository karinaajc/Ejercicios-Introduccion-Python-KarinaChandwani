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

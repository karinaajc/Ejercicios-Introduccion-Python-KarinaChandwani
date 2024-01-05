def Sumar(x, y):
    return x + y

def Restar(x, y):
    return x - y

def Multiplicar(x, y):
    return x * y

def Dividir(x, y):
    if y != 0:
        return x / y
    else:
        return 'MATH ERROR'

def Potencia(x, y):
    return x ** y

def RaizCuadrada(x):
    if x >= 0:
        return x ** 0.5
    else:
        return 'MATH ERROR'

def calculadora():
    print("¡Bienvenido a la calculadora de Karina!")
    
    while True:
        eleccion_de_operacion = input('Selecciona una operación (Sumar(1) / Restar(2) / Multiplicar(3) / Dividir(4) / Elevar un numero a otro(5) / Raiz Cuadrada(6) / Salir(7)): ')
        
        if eleccion_de_operacion == '7':
            break

        if eleccion_de_operacion in ['1', '2', '3', '4', '5']:
            x = float(input('Introduce el primer numero: '))
            y = float(input('Introduce el segundo numero: '))

            if eleccion_de_operacion == '1':
                result = Sumar(x, y)
            elif eleccion_de_operacion == '2':
                result = Restar(x, y)
            elif eleccion_de_operacion == '3':
                result = Multiplicar(x, y)
            elif eleccion_de_operacion == '4':
                result = Dividir(x, y)
            elif eleccion_de_operacion == '5':
                result = Potencia(x, y)
        elif eleccion_de_operacion == '6':
            x = int(input('Introduce el primer numero sobre el que realizar la raiz cuadrada: '))
            result = RaizCuadrada(x)
        else:
            print(f'{eleccion_de_operacion} No es una opción válida')

        print('Resultado:', result)

if __name__ == "__main__":
    calculadora()

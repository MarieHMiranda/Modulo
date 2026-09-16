#retorna verdadero si el número ingresado es par
def es_par(numero):
    par = numero % 2 == 0
    return par

#retorna el doble del número ingresado
def el_doble(numero):
    doble = numero * 2
    return doble

#retorna el promedio de la lista de números
def promedio(lista_numeros):
    prom = sum(lista_numeros) / len(lista_numeros)
    return prom

#retorna el área del círculo a partir del radio ingresado
def area_circulo(radio):
    pi = 3.14159
    area = pi * radio ** 2
    return area

#retorna verdader si el primer número es mayor al segundo
def mayor_que(numero1, numero2):
    ok = numero1 > numero2
    return ok

#retorna la suma de los tres números
def suma(num1,num2,num3):
    suma = num1 + num2 + num3
    return suma
    

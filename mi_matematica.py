# ✅ Bien hecho: comparación booleana clara, y se devuelve directo sin ifs innecesarios.
#retorna verdadero si el número ingresado es par
def es_par(numero):
    par = numero % 2 == 0
    return par

#retorna el doble del número ingresado
def el_doble(numero):
    doble = numero * 2
    return doble

# ✅ Bien hecho: buen uso de sum() y len(), evita reinventar la suma con un for.
# 💡 Sugerencia: si lista_numeros llega vacía, len() da 0 y esto explota con ZeroDivisionError.
# No hace falta resolverlo para este ejercicio, pero es bueno tenerlo en cuenta a futuro.
#retorna el promedio de la lista de números
def promedio(lista_numeros):
    prom = sum(lista_numeros) / len(lista_numeros)
    return prom

# 💡 Sugerencia: como este ejercicio es justamente sobre módulos, este es un buen lugar
# para practicar "import math" y usar math.pi en vez de escribir 3.14159 a mano.
#retorna el área del círculo a partir del radio ingresado
import math

def area_circulo(radio):
    pi = math.pi
    area = pi * radio ** 2
    return area

# ❌ Error: el comentario dice "retorna verdader", falta la "o" final (retorna verdadero).
#retorna verdader si el primer número es mayor al segundo
def mayor_que(numero1, numero2):
    ok = numero1 > numero2
    return ok

# 💡 Sugerencia: dos detalles de estilo, sin ser errores:
# 1) falta espacio después de cada coma en los parámetros (num1, num2, num3), por PEP 8.
# 2) la variable "suma" tiene el mismo nombre que la función; funciona porque su alcance
#    es local, pero puede confundir en funciones más largas. Un nombre como "resultado" es más claro.
#retorna la suma de los tres números
def suma(num1,num2,num3):
    suma = num1 + num2 + num3
    return suma
    

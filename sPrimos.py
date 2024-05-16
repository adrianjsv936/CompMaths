from primos import *
from mcd import mcd2

def Usus(a):
    pares = []
    primos = []
    for i in range(2,a+1):
        for j in range(2,i):
            if mcd2(i,j) == 1:
                tupla = (i,j)
                pares.append(tupla)
    for m in pares:
        for k in range(0,a+1):
            num = m[0]*k + m[1]
            if primo(num) == True:
                count = 0
                for p in primos:
                    if num == p:
                        count += 1 
                if count == 0:
                    primos.append(num)
    primos = sorted(primos)
    return primos

def intento(rango):
    x = Usus(rango)
    y = lista_primos(rango*50)
    for i in range(0,len(y)):
        if x[i] != y[i]:
            print('No se cumple')
            return False
            break
    return True        

def sucesiones(a,b,n):
    primos = []
    for x in range(0,n+1):
        num = a*x + b
        if primo(num) == True:
            count = 0
            for p in primos:
                if num == p:
                    count += 1 
            if count == 0:
                primos.append(num)
    primos = sorted(primos)
    return primos
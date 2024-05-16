#algoritmo para calcular el mcm de n numeros.
from mcd import mcd2
def mcm(opc):
    opc = 1  
    list = []
    while opc == 1:
        print("escribe el numero")
        a = input()
        a = int(a)
        list.append(a)
        print("quieres agregar mas numeros?")
        opc =  input()
        opc = int(opc)
    mcm = 0 
    while len(list) > 1:
        reserva = list
        q = mcd2(list[0],list[1])
        mcm = (abs(list[0]*list[1]))/q   
        list = []
        list.append(mcm)
        i = 2
        while i < len(reserva):
            list.append(reserva[i])
            i += 1   
    g = list[0]
    return g
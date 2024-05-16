#algoritmo para calcular el mcd de 2 numeros.
def mcd2(a, b):
    n = 0
    r = 1
    if a > b:
        n = b
        b = a
        a = n
    while r != 0:
        r = b % a
        if r != 0:
            b = a
            a = r 
    q = a
    return q
#algoritmo para calcular el mcd de n numeros
def n_mcd(opc):
    opc = 1  
    list = []
    while opc == 1:
        print("escribe el numero")
        x = input()
        x = int(x)
        list.append(x)
        print("quieres agregar mas numeros?")
        opc =  input()
        opc = int(opc) 
    while len(list) > 1:
        reserva = list
        q = mcd2(list[0],list[1])
        list = []
        list.append(q)
        i = 2
        while i < len(reserva):
            list.append(reserva[i])
            i += 1   
    h = list[0]
    return h
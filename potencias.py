# a es la base, n es la cantidad de potencias a calcular
def potencia(a,n):
    list = []
    for k in range(1,n):
        list.append(a**k)
    return list
def l_digit(a,k):
    mod = a % 10
    opc = {1:1, 2:4, 3:4, 4:2, 5:1, 6:1, 7:4, 8:4, 9:2}
    res_1 = k % (opc.get(mod))
    residuos = {1:[1], 2:[6,2,4,8], 3:[1,3,9,7], 4:[6,4], 5:[5], 6:[6], 7:[1,7,9,3], 8:[6,8,4,2], 9:[1,9]}
    new = residuos.get(mod)
    res = new[res_1]
    return res
print(l_digit(0,0)) 
    
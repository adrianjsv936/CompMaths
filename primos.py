def lista_primos(n):
    list_primos = []
    for i in range(2,n+1):
        div = 0
        for j in range(2,i+1):
            if i%j == 0:
                div += 1
        if div == 1:
            list_primos.append(i)
    return list_primos

def primo(a):
    div = 0
    for j in range (2,a+1):
        if a%j == 0:
            div += 1
    if div == 1:
        return True
    else:
        return False
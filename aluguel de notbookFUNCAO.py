import pytest

def calcula_reservas(reservas):
    if len(reservas) == 0:
        return 0

    maior = max(i[1] for i in reservas) +1
    menor = min(i[0] for i in reservas) 

    cont = 0

    for j in range(menor,maior):
        aux = 0
        for i in reservas:
            if j in range(i[0],i[1]):
                aux += 1
            if aux > cont:
                cont = aux
    return cont 

calcula_reservas(5)

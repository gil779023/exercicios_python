def calcula_reservas(reservas):
    hora = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(reservas)):
        j = min(reservas[i])
        k = max(reservas[i])
        p = j
        for p in range(j,k):
            hora[p]=hora[p]+1
    h = max(hora) 
    return (h)  
print(calcula_reservas(2,3))             
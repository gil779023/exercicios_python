def buscar_carro(carros,donos,dono):
    for i in range(len(donos)):
        if donos == donos[i]:
            return carros[i]
    return 'sem carro'        




carros =  ['corsa','classic','corolla']
donos = ['reinaldo','joao','edinei']

dono = input('qual o dono:')
carro = buscar_carro(carros,donos,dono)
print(f'o carro de{dono} e {carro}')


#cadastro


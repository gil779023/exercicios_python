from pickle import NONE


donos =[ ['reinaldo','corsa'],
        ['joao','classic',],
        ['edinei','corola']]

def busca_carro(donos,dono):
    for par in donos:
        if par[0] == dono:
            return par[1]   
    return NONE

dono ='edinei' 
carro = busca_carro(donos,dono)  
print(f'o carro de {dono} e {carro}')


#dicionarios


donos = {
    'reinaldo':'corsa',
    'joao':'classic',
    'ednei':'corolla'
}

def busca_carros(donos,dono):
    return donos[dono]
    
    
dono = input('qual o dono:')
print(busca_carros(donos,dono))


for i in donos.values():
    print(i)

    


for dono,carro in donos.itens(): 
    print(dono,carro)




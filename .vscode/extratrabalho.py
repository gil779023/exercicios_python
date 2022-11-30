 
def vender_automovel():
    arquivo = []
    clien = []
    vend = []
    a = "s"
    while a.lower() == "s":
        with open('cadcarros.txt','r') as arquivo:
        
            for arq in arquivo:
                
                with open('cadcliente.txt','r') as clien:
                    cont = 0
                    for h in clien:
                        
                        with open('cadvendedor.txt','r') as vend:
                            for j in vend:
                                
                                carros_vendidos = [] 
 
                                compra = input('qual carro sera vendido? :')
                                dono = input('quem comprara o carro? :')
                                vendedor = input('qual vendedor fara a venda ao cliente? :')
                                carros_vendidos =[]
                                clientes_atendidos = []
                                vendas_efetuadas = []
                                if arq[0] != compra:
                                    cont += 1
                                    carros_vendidos = compra
                                    arq.del(compra) 
                                if h[0] != dono:
                                    cont += 1
                                    clientes_atendidos = dono
                                if j[0] != vendedor:
                                    cont += 1
                                    vendas_efetuadas = vendedor
                                   
                                a = input ("Deseja escolher outro carro? s/n  :")
                                print(vendas_efetuadas,clientes_atendidos,carros_vendidos)
                                print(f'o vendedor : {vendas_efetuadas} vendeu o carro : {carros_vendidos} para o cliente : {clientes_atendidos}')                                
                                break    
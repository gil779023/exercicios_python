  vend = []
                                        funcionario = str(input('qual funcionario ira atende-lo? : '))    
                                        if funcionario != j[0]:
                                            cont +=1 
                                            atendimento = funcionario
                                            a = input ("Deseja escolher outro vendedor? s/n :")
                                            print(f' o vendedor {atendimento} vendeu o carro  {carros_vendidos} para o cliente {clientes_atendidos}')
                                            break
                                        
                                        
                                         clien = []       
                            nome = str(input('qual cliente sera atendido? :'))   
                            if nome != h[0]:
                                cont += 1 
                                clientes_atendidos = nome 
                                a = input ("Deseja escolher outro s/n :")
                                with open('cadvendedor.txt','r') as vend:
                                    cont = 0
                                    
                                    carros_vendidos = [] 
                escolha = str(input('qual carro sera vendido ao cliente  :'))   
                if escolha != arq[0]:
                    cont += 1
                    carros_vendidos = escolha
                    a = input ("Deseja escolher outro carro? s/n  :")      
                    with open('cadcliente.txt','r') as clien:
                        cont = 0
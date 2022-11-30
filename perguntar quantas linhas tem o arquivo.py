


arq = open('nomes_formatado.txt','w')
nomes = []
for i in range(5):
    nome = str(input(f'digite {i+1} nomes:  '))
    nomes.append(nome)
    nome.upper()
    nome.split()
    arq.write('\n')
    if nomes == 5:
        break    
arq.write(f'{nomes}\n')
arq.close() 


#Faça um programa que pergunta ao usuário o nome de um arquivo. Em seguida, 
# o programa deve informa quantas linhas o arquivo possui.
cont = 0
arq = input('qual nome do arquivo  que voce procura ?   ')
#if arq == 'nomes_formatado' :
arquivo = open(arq,'r')
for i in arq:
    cont += 1
    
print(cont)
arquivo.close()
 
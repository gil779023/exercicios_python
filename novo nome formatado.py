import importlib


#Leia o arquivo `nomes.txt`, e formate os nomes de maneira
#  que apenas a primeira letra de cada nome seja maiúscula. Grave os nomes em um arquivo chamado `nome_formatado.txt

arq = open('nomes_formatado.txt','w')

nomes = []
for i in range(5):
    nome = str(input('digite 5 nomes: '))
    nomes.append(nome)
    nome.upper()
    nome.split()
    
    if nomes == 5:
        break    
arq.write(f'{nomes}\n')
arq.close()
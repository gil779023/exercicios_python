
#Peça ao usuário que digite 5 nomes. Em seguida, grave os nomes em um arquivo chamado nomes.txt.



'''arq = open('nomes.txt','w')

nomes = []
for i in range(5):
    nome = str(input('digite 5 nomes: '))
    nomes.append(nome)
    if nomes == 5:
        break    
arq.write(f'{nomes}\n')
arq.close()  '''






#Peça ao usuário que digite um número N. Depois, peça que digite N nomes. Em seguida, grave os nomes em um arquivo chamado nomes.txt.




arq = open('nomes.txt','w')




n = 5
for i in range(n):
    nome = str(input('digite N nomes: '))

    arq.write(f'{nome}\n')
arq.close()  









menor = 0
maior = 0
soma = 0
qtd = 1
num = 0
while num >= 0:
    num = int(input('digite numeros   :'))  
    if num < 0:
        break 
    soma = soma + num
    qtd +=1
    media = soma / qtd
    if qtd == 1:
        soma = soma = num   
    if num > maior:
        maior = num
    if num < menor:
        menor = num              
print(f'O maior numero foi  {maior}\nO menor numero foi  {menor}')
print(f'a media e {media}')
    
    


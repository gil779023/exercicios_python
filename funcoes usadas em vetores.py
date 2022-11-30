'''pares=[2,4,6,8]
vogais=['a','e','i','o','u']
print(pares+vogais)
print(vogais*3)
print(5 in pares)
print('a' not in vogais)'''



frase='  um EXEMPLO interessante.  '
print(frase.capitalize())
print(frase.lower())
print(frase.upper())
print(frase.islower())
print(frase.isupper())
print(frase.split(' '))
print(frase.find('inter'))
print(frase.replace('inter','estr'))
print(frase.strip())
#.capitalize(): converte a primeira letra para maiúscula;
#.lower(): converte as letras para minúsculas;
#.isupper(): verifica se todas os caracteres são letras maiúsculas;
#.split(): divide em várias outras strings, de acordo com algum caractere de separação;
#.find(b): retorna a posição string a aparece;
#.replace(a, b): substitui na string as substrings a por b;
#.strip(): remove espaços existentes no início e fim da string;
#.format(): formata a string, podendo realizar substituição de variáveis.

valor1, valor2, soma = 25,5,30
print('A soma de {} e {} é {}.'.format(valor1, valor2, soma))
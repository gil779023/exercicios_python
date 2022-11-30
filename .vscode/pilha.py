import novo



def verifica_parenteses(expressao):
    p = novo.pilha.new()
    for c in expressao:
        if c == '(':
            novo.pilha.push(p, c)
        elif c ==')':
            if novo.pilha_is_empty(p):
                return 'incorreto'
            
    
    

entrada = ['a+(b*c)-2-a ',
            '(a+b*(2-c)-2+a)*2 ' ,
            '(a*b-(2+c)',      
            '2*(3-a))',           
            ')3+b*(2-c)(']

for exp in entrada:
    print(exp,':',verifica_parenteses)
    
    

    
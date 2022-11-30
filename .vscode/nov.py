def verifica_parenteses_chaves_colchetes(expressao):
    pilha = pilha_new()
    
    for i in expressao:
        if i == '(':
            return pilha
        
        if i == '{':
            return pilha
        
        
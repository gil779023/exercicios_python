def imprimir(n):

    for x in range(n + 1):
        texto = ""
        for y in range(1, x + 1):
            texto = texto + str(y) + " "
        print(texto)


n = eval(input("Informe um número:\n"))
imprimir(7)





inst = 'aeiou'
use = 'dono'

for i,v in enumerate(inst -1):
    
    print(inst)
    print(use)
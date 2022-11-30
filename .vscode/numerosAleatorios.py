import random


arq = open('numeros.txt','w')
r=""
for i in range(10):
    p = random.randint(0,100) 
    p_string = str(p)
    r += p_string + '\n'
arq.write(r)   
arq.close() 

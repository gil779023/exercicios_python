
def primo(p):
    cont = 0
    for i in range(1,p):
        if p % i == 0:
            cont +=1
        if cont == 1:
            return True 
    return False       






def test_primo():
    #assert primo(7) == True
    assert primo(2) == True
    #assert primo(17) == True
    #assert primo(28) == False
   # assert primo(100) == False
try:
    test_primo()
    print('ok')
except:
    print('nao')    
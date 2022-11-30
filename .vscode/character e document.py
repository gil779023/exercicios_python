
 # for c in set(document):
#        if document.count(c) > characters.count(c):
 #           return False
#    return True
#print(string('asdfgdfhf','asd'))  
  



def letra(characters,document):
    contadores = dict()


    for c in characters:
        if c not in contadores:
            contadores [c] = 1
        else:
             contadores[c]+=1

    for c in document:
        if c not in contadores:
            return False
        else:
            if contadores[c] == 0:
                return False
            contadores[c] -=1    
    return True  






def primo(p):
    if p % 2 != 0:
        return True
    else:
        return False
         
print(primo(7))
print(primo(2))
print(primo(17))
print(primo(28)) 
print(primo(100))        
def test():

    assert(letra('asdfdfdhgfjgd','asd')) == True

try:
    test()
    print('ok')



except:
    print('no')    

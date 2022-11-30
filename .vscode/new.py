def  menu de entradas ():
    x  =  float ( input ( "Digite um número \n " ))
    y  =  float ( input ( "Digite um outro número \n " ))
    menu ( x , y )


 menu def ( x , y ):
    escolha  =  int ( entrada ( '''
        Qual operação matemática você deseja fazer com %de %d ?
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Exponenciação
0 - Para voltar ao menu
Escolha: '''  % ( x , y )))
    se  escolha  ==  1 :
        print ( 'A soma de ' , x , ' e ' , y , 'é igual a ' , x  +  y , '.' , sep = '' )
        passar
    elif  escolha  ==  2 :
        print ( 'A subtração de ' , x , ' e ' , y , 'é igual a ' , x  -  y , '.' , sep = '' )
        passar
    elif  escolha  ==  3 :
        print ( 'A multiplicação de ' , x , ' e ' , y , 'é igual a ' , x  *  y , '.' , sep = '' )
        passar
    elif  escolha  ==  4 :
        print ( 'A divisão de ' , x , ' e ' , y , 'é igual a ' , x  /  y , '.' , sep = '' )
        passar
    elif  escolha  ==  5 :
        print ( x , 'elevado a ' , y , 'é igual a ' , x  **  y , '.' , sep = '' )
        passar
    elif  escolha  ==  0 :
        passar
    mais :
        print ( " \n Este número não está nas alternativas, tente novamente :D." , sep = '' )
        menu ( x , y )


def  inputlinear ():
   tente :
    print ( "Digite os valores para as incógnitas e pressione Enter para a incógnita de valor desconhecido" )
    y  =  input ( "Digite um valor para y. \n " )
    se  y . isdigit ():
        y  =  int ( y )
    a  =  input ( "Digite um valor para a. \n " )
    se  um . isdigit ():
        a  =  int ( a )
    x  =  input ( "Digite um valor para x. \n " )
    se  x . isdigit ():
        x  =  int ( x )
    b  =  input ( "Digite um valor para b. \n " )
    se  b . isdigit ():
        b  =  int ( b )
    linear ( y , a , x , b )
   exceto  TypeError :
    print ( "É preciso valores a três variáveis. \n " )


def  linear ( y , a , x , b ):
    if  tipo ( y ) ==  str :
        print ( "y=%d*%d+%d"  % ( a , x , b ))
        print ( "y é igual a %f"  % ( a  *  x  +  b ))
    if  tipo ( a ) ==  str :
        print ( "%d=a*%d+%d"  % ( y , x , b ))
        print ( "a é igual a %f"  % (( y  -  b ) /  x ))
    if  tipo ( x ) ==  str :
        print ( "%d=%d*x+%d"  % ( y , a , b ))
        print ( "x é igual a %f"  % (( y  -  b ) /  a ))
    if  tipo ( b ) ==  str :
        print ( "%d = %d*%d + b"  % ( y , a , x ))
        print ( "b é igual a %f"  % ( y  -  a  *  x ))


def  dualidade ():
    c = int ( input ( "Digite um número para identificar se é par ou ímpar. \n " ))
    se  c  %  2  ==  0 :
        print ( "%d é par"  %  c )
    mais :
        print ( "%d é ímpar"  %  c )


def  mult ():
    e  =  int ( input ( "Digite um número natural para saber se é múltiplo de um próximo número. \n " ))
    d  =  int ( input ( "Digite um outro número. \n " ))
    se  d  %  e  ==  0 :
        print ( "%d é múltiplo de %d!"  % ( d , e ))
    mais :
        print ( "%d não é múltiplo de %d!"  % ( d , e ))


def  menuprinc ():
    opcao = int ( entrada ( '''
    	  Escolha um programa
1 - Calculadora Simples
2 - Função Linear
3 - Par ou ímpar
4 - Múltiplo
0 - Fechar Menu
Escolha: ''' ))
    if  opcao  ==  1 :
        menu de entradas ()
    elif  opcao  ==  2 :
        entradas lineares ()
    elif  opcao  ==  3 :
        dualidade ()
    elif  opcao  ==  4 :
        múltiplo ()
    elif  opcao  ==  0 :
        sair ()
    mais :
        print ( "Este número não está nas alternativas, novamente tente :D. \n " )
        menuprinc ()
enquanto  Verdadeiro :
    tente :
        menuprinc ()    
    exceto  ZeroDivisionError :
        print ( "Não é possível fazer divisão por zero, tente novamente :D. \n " )
    exceto  ValueError :
        print ( "Isso não é um número, tente novamente :D. \n " )
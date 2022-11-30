produto1 = ['arroz', 10, 13.45]
produto2 = ['feijao' , 2, 7.50]
produto3 = [ 'trigo', 40, 15.09]
compras = [produto1,produto2,produto3]
for e in compras:
    print(f'produto {e[0]}')
    print(f'produto {e[1]}')
    print(f'produto {e[2]:5.2f}')
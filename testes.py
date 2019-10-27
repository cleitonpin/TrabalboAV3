import random

pos = 0
while pos == 0:
    codigo_campeonato = random.randrange(1001, 9999)
    cod_Campeonato = input(f'Insira o código do campeonato [{codigo_campeonato}] -> ')

    if cod_Campeonato.iscn== True:
        if cod_Campeonato != codigo_campeonato:
            print('Código errado, digite novamente')
            continue
        elif cod_Campeonato == codigo_campeonato:
            print('Correto')
            pos = 1
    else:
        print('Apenas números!')
        continue


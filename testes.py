import random

a = 0
while a ==0:
    contato = input('Insira seu email para contato -> ')

    verificaremail = (contato.find('@'),contato.find('.com'))

    if verificaremail[0] == -1 or verificaremail[1] == -1:
        print('email invalido')
        continue

print('issae')
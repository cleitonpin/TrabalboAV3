
back = 0
while back == 0:
    tel = input(f'Digite o número [+DDD][8212345678] -> +')

    print (tel.isnumeric())
    
    if tel.isnumeric() == True:
        print('Vinculado com sucesso')
        back = 1
    else:
        print('Apenas números!')
        continue
import bd1

def criarconta():
    cont = 0 
    while cont == 0:
        usuario = input('Insira seu usuario: ')
        senha = input('Insira sua senha: ')
        email = input('Insira um e-mail válido: ')
        datanasc = input('Insira sua data de nasimento [dd/mm/yyyy]: ')
        nick = input('Insira seu nick: ')

        verificaremail = (email.find('@'),email.find('.com')) 

        if verificaremail[0] == -1:
            print("\n\nErro: email inválido [ausência de: '@']\n")
            continue
        if verificaremail[1] == -1:
            print("\n\nErro: email inválido [ausência de: '.com/.com.br/...']\n")
            continue
        if len(usuario) <= 4:
            print('Número de caracteres insuficiente[minimo 4]\n')
            continue
        elif len(usuario) >= 12:
            print('Número de caracteres acima do indicado[máximo de 12]\n')
            continue
        bd1.cursor.execute("select usuario from usuarios where usuario = %s", (usuario,))
        rowUsuario = bd1.cursor.rowcount 
        bd1.cursor.execute("select nick from usuarios where nick = %s", (nick,))
        rowNick = bd1.cursor.rowcount 

        row= (rowUsuario, rowNick)
        if row[0] > 0 or row[1] > 0:
            if row[0] > 0:
                print('ERROR: Usuário já existe')
            if row[1] > 0:
                print('ERROR: Nick já existe')      
        else: 
            bd1.cursor.execute("insert into usuarios(email,usuario,nick,datanasc,senha) values(%s,%s,%s,%s,%s)",(email,usuario,nick,datanasc,senha))
            bd1.connection.commit()
            print('Úsuario cadastrado com sucesso')
            cont = 1 
    
        


def Entrar():
    pop = 0
    while pop == 0:
        usuario = input('Úsuario: ')
        senha = input('Senha: ')

        bd1.cursor.execute("SELECT usuario,senha FROM usuarios WHERE usuario=%s AND senha=%s",(usuario, senha))
        numRow = bd1.cursor.rowcount
        
        if numRow > 0:
            #usuário logado
            print('-> Sair\n-> Cadastrar time\n-> Times registrados\n-> Configurações\n-> Vincular telefone')
            ops = input()
            # if ops == 'configurações':
            #     bd1.cursor.execute("SELECT email FROM usuarios WHERE email = %s",(recebeEmail,))
            #     emailBD = bd1.cursor.fetchall()
            #     print(f'Email cadastrado -> {emailBD[0]}')

            if ops == 'vincular telefone':
                back = 0
                while back == 0:
                    tel = input('Digite o número [+DDD][8212345678] -> +')
        
                    if tel.isnumeric() == True:
                     
                        
                        row = bd1.cursor.rowcount
                        if row[0]:
                            bd1.cursor.execute(f"insert into usuarios(telefone) values({tel})")
                            bd1.connection.commit()
                            print('Vinculado com sucesso')
                            back = 1
                    else:
                        print('Apenas números!')
                        continue


        else:
            print("Usuário ou senha incorretos!\n")
            continue
    
    #mostra email
    
    #aqui tu bota o q tu quiser, menu sla



conti = 0


while conti == 0:
    print('-> Ver times\n-> Cadastrar\n-> Categorias\n-> Criar Conta\n-> Entrar')
    opc = input()

    if opc == 'criar conta':
        criarconta()
        continue
    elif opc == 'entrar':
        Entrar()

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
            print("\n\nErro: email inválido [missing: '@']\n")
            continue
        if verificaremail[1] == -1:
            print("\n\nErro: email inválido [missing: '.com/.com.br/...']\n")
            continue
        if len(usuario) <= 4:
            print('Número de caracteres insuficiente[minimo 4]')
            continue
        elif len(usuario) >= 12:
            print('Número de caracteres acima do indicado[máximo de 12]')
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
        
        
        # if rowNick > 0:
        #     print('ERROR: Nick já existe')
        # else: 
        #     bd1.cursor.execute("insert into usuarios(email,usuario,nick,datanasc,senha) values(%s,%s,%s,%s,%s)",(email,usuario,nick,datanasc,senha))
        #     bd1.connection.commit()
        #     print('Úsuario cadastrado com sucesso')
        #     cont = 1
        #     bd1.cursor.close()
##arquivo = open('times.txt','r')
print('1 - Entrar\n2 - Sair\n')
conta = input()
if conta == 'entrar':
    print('Login efetuado com sucesso\n\n1 - Ver times\n2 - Cadastrar\n3 - Categorias\n4 - Criar Conta')
    opc = input()

if opc == 'criar conta':
    criarconta()
import bd1
import random

def criarconta():
    cont = 0 
    while cont == 0:
        telefone = 0
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
        if len(usuario) < 4:
            print('Número de caracteres insuficiente[mínimo 4]\n')
            continue
        elif len(usuario) > 12:
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
            bd1.cursor.execute("insert into usuarios(telefone,email,usuario,nick,datanasc,senha) values(%s,%s,%s,%s,%s,%s)",(telefone,email,usuario,nick,datanasc,senha))
            bd1.connection.commit()
            print('Úsuario cadastrado com sucesso')
            cont = 1 
    
def registrarCampeonato():
    cont1 = 0
    while cont1 == 0:
        codigo_campeonato = random.randrange(1001, 9999)
        cod_Campeonato = input(f'Insira o código do campeonato [{codigo_campeonato}] -> ')

        if cod_Campeonato.isnumeric() == True:
            bd1.cursor.execute("select cod_campeonato from campeonatos where cod_campeonato = %s", (cod_Campeonato,))
            bdcod_camp = bd1.cursor.rowcount
            if int(cod_Campeonato) != int(codigo_campeonato) or bdcod_camp > 0:
                print('Código errado ou já usado, digite novamente.')
                continue
            elif int(cod_Campeonato) == int(codigo_campeonato):
                print('Correto')
                cont1 = 1
        else:
            print('Apenas números!')
            continue
    nome_Campeonato = input('Insira o nome do campeonato -> ')
    data_inicio = input('Insira a data de ínicio [dd/mm/yyyy] -> ')
    data_fim = input('Insira a data final [dd/mm/yyyy] -> ')
    categoria = input('Insira a categoria -> ')

    bd1.cursor.execute("insert into campeonatos(cod_campeonato,nome,data_inicio,data_fim,categoria) values(%s,%s,%s,%s,%s)",(cod_Campeonato,nome_Campeonato,data_inicio,data_fim,categoria))
    bd1.connection.commit()
    print('Campeonato registrado.')
           
def VerCamp():
    cod_camps = int(input('Insira o código do campeonato -> '))

    bd1.cursor.execute("select cod_campeonato from campeonatos where cod_campeonato = %s", (cod_camps,))
    bdcod_camps = bd1.cursor.rowcount

    if bdcod_camps > 0:
        print('verificado')
    else:
        print('Campeonato inexistente.')


def Entrar():
    
    usuario = input('Úsuario: ')
    senha = input('Senha: ')
    pop = 0
    while pop == 0:

        bd1.cursor.execute("SELECT usuario,senha FROM usuarios WHERE usuario=%s AND senha=%s",(usuario, senha))
        numRow = bd1.cursor.rowcount
        print('-> Sair\n-> Times registrados\n-> Configurações\n-> Vincular telefone')
        ops = input()
        if ops == 'sair':
            pop = 1
        if numRow > 0:
            #usuário logado
            

           
        
            # if ops == 'configurações':
            #     bd1.cursor.execute("SELECT email FROM usuarios WHERE email = %s",(recebeEmail,))
            #     emailBD = bd1.cursor.fetchall()
            #     print(f'Email cadastrado -> {emailBD[0]}')

            if ops == 'vincular telefone':
                back = 0
                
                while back == 0:
                    tel = input('Digite o número [+DDD][8212345678] -> +')
                    
                    if len(tel) > 13:
                        print('Número passou do limite [11 Números]')
                        continue

                    if tel.isnumeric() == True : 
                        bd1.cursor.execute("select telefone from usuarios where usuario = %s",(usuario,))  
                        pegar = bd1.cursor.fetchall()
                        if pegar[0] == 0:
                            bd1.cursor.execute("update usuarios set telefone = %s where usuario = %s",(tel,usuario,))
                            bd1.connection.commit()
                            print('Vinculado com sucesso')
                            pop = 1
                            
                        else:
                            bd1.cursor.execute("select telefone from usuarios where usuario = %s",(usuario,))  
                            bdTelefone = bd1.cursor.fetchall()
                            
                            print(f'Conta já vinculada com telefone {bdTelefone[0]}') 
                            back = 1                 
                    else:
                        print('Apenas números!')
                        continue

            

        else:
            print("Usuário ou senha incorretos!\n")
            continue


conti = 0


while conti == 0:
    print('-> Entrar\n-> Criar Conta\n-> Plataformas\n-> Registrar campeonato\n-> Ver campeonatos [ativos]')
    opc = input()

    if opc == 'criar conta':
        criarconta()
        continue
    elif opc == 'entrar':
        Entrar()
        continue
    elif opc == 'registrar campeonato':
        registrarCampeonato()
        continue
    elif opc == 'ver campeonatos':
        VerCamp()
        exit()
        
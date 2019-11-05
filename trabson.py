import bd1
import random
import time
import os 

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

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


nomeDaEquipe=''
def registrarEquipes():
    global nomeDaEquipe

    a = 0 

    while a == 0:

        nomeORGANIZADOR = input('Insira seu nome pessoal -> ')
        Endereço = input('Insira seu endereço -> ') 
        contato = input('Insira seu email (válido) para contato -> ')
        pessoa = int(input('Cadastrar a equipe como: Pessoa Física [1] ou Juridíca [2] -> '))

        verificaremail = (contato.find('@'),contato.find('.com'))

        if verificaremail[0] == -1:
            print("\n\nErro: email inválido [ausência de: '@']\n")
            continue
        if verificaremail[1] == -1:
            print("\n\nErro: email inválido [ausência de: '.com/.com.br/...']\n")
            continue

        if pessoa == 1:
            
            nomeEquipe = input('Insira o nome da equipe que deseja inscrever no campeonato -> ')
            nomeDaEquipe = nomeEquipe
            nomeTreinador = input('Insira o nome do treinador -> ')
            topLaner = input('\nExemplo nome -> Flavio "Jukes" Fernandes\n\nNome do top laner [Nome "Nick" Sobrenome] -> ')
            jungle = input('Nome do jungle [Nome "Nick" Sobrenome] -> ')
            midLaner = input('Nome do mid laner [Nome "Nick" Sobrenome] -> ')
            atirador = input('Nome do atirador [Nome "Nick" Sobrenome] -> ')
            suporte = input('Nome do suporte [Nome "Nick" Sobrenome] -> ')
            reserva = input('Há reservas s/n? ')

            if reserva == 's':
                print('Pode apenas 1 reserva\n')
                nomeReserva = input('Insira o nome e a lane [Flavio "Jukes" Fernandes]-[TopLaner] -> ')      
                 
                cpf = input('Insira seu cpf (XXX.XXX.XXX-XX) -> ')
                
                if len(cpf) > 11 or len(cpf) < 11:
                    print ('Valores inseridos esta fora do padrão, por favor tente novamente.')
                    continue  
                else:

                    bd1.cursor.execute("insert into organizadorpessoa(nome,contato,endereço) values(%s,%s,%s)",(nomeORGANIZADOR,contato,Endereço))
                    bd1.connection.commit()

                    bd1.cursor.execute("insert into equipes(nomeequipe,toplaner,midlaner,jungler,atirador,suport,treinador,reservas) values(%s,%s,%s,%s,%s,%s,%s,%s)",(nomeEquipe,topLaner,midLaner,jungle,atirador,suporte,nomeTreinador,nomeReserva))                
                    bd1.cursor.execute("select id_pessoa from organizadorpessoa WHERE NOME = %s", (nomeORGANIZADOR,))
                    id_pessoa = bd1.cursor.fetchall()
 
                    bd1.cursor.execute("insert into pessoafisica(id_pessoa,cpf) values(%s,%s)", (id_pessoa[0],cpf))
                    bd1.connection.commit()
                    print('Equipe cadastrada com sucesso.')
                    a = 1 
            else:
                cpf = input('Insira seu cpf (XXX.XXX.XXX-XX) -> ')
                
                if len(cpf) > 11 or len(cpf) < 11:
                    print ('Valores inseridos esta fora do padrão, por favor tente novamente.')
                    continue  
                else:                                  
                    bd1.cursor.execute("insert into organizadorpessoa(nome,contato,endereço) values(%s,%s,%s)",(nomeORGANIZADOR,contato,Endereço))
                    bd1.connection.commit()
                    bd1.cursor.execute("insert into equipes(nomeequipe,toplaner,midlaner,jungler,atirador,suport,treinador) values(%s,%s,%s,%s,%s,%s,%s)",(nomeEquipe,topLaner,midLaner,jungle,atirador,suporte,nomeTreinador))                
                    bd1.cursor.execute("select id_pessoa from organizadorpessoa WHERE NOME = %s", (nomeORGANIZADOR,))
                    id_pessoa = bd1.cursor.fetchall()
 
                    bd1.cursor.execute("insert into pessoafisica(id_pessoa,cpf) values(%s,%s)", (id_pessoa[0],cpf))
                    bd1.connection.commit()
                    print('Equipe cadastrada com sucesso.')
                    a = 1 
                
        else:


            nomeEquipe = input('Insira o nome da equipe que deseja inscrever no campeonato -> ')
            nomeDaEquipe = nomeEquipe
            nomeTreinador = input('Insira o nome do treinador -> ')
            topLaner = input('\nExemplo nome -> Flavio "Jukes" Fernandes\n\nNome do top laner [Nome "Nick" Sobrenome] -> ')
            jungle = input('Nome do jungle [Nome "Nick" Sobrenome] -> ')
            midLaner = input('Nome do mid laner [Nome "Nick" Sobrenome] -> ')
            atirador = input('Nome do atirador [Nome "Nick" Sobrenome] -> ')
            suporte = input('Nome do suporte [Nome "Nick" Sobrenome] -> ')
            reserva = input('Há reservas s/n? ')

            if reserva == 's':
                print('\nPode apenas 1 reserva\n')
                nomeReserva = input('Insira o nome e a lane [Flavio "Jukes" Fernandes][TopLaner] -> ')      
                 
                cnpj = input('Insira seu CNPJ (XX.XXX.XXX/XXXX.XX) -> ')
                
                if len(cnpj) > 14 or len(cnpj) < 14:
                    print ('Valores inseridos esta fora do padrão, por favor tente novamente.')
                    continue  
                else:
                    
                    #pegando foreign key

                    bd1.cursor.execute("insert into organizadorpessoa(nome,contato,endereço) values(%s,%s,%s)",(nomeORGANIZADOR,contato,Endereço))
                    bd1.connection.commit()
                    
                    bd1.cursor.execute("insert into equipes(nomeequipe,toplaner,midlaner,jungler,atirador,suport,treinador,reservas) values(%s,%s,%s,%s,%s,%s,%s,%s)",(nomeEquipe,topLaner,midLaner,jungle,atirador,suporte,nomeTreinador,nomeReserva))
                    bd1.cursor.execute("select id_pessoa from organizadorpessoa WHERE NOME = %s", (nomeORGANIZADOR,))
                    id_pessoa = bd1.cursor.fetchall()[0]
                    bd1.cursor.execute("insert into pessoajuridica(id_pessoa,cnpj) values(%s,%s)", (id_pessoa,cnpj))
                    bd1.connection.commit()
                    print('Equipe cadastrada com sucesso.')
                    a = 1 
            else:
                cnpj = input('Insira seu CNPJ (XX.XXX.XXX/XXXX.XX) -> ')
                
                if len(cnpj) > 14 or len(cnpj) < 14:
                    print ('Valores inseridos esta fora do padrão, por favor tente novamente.')
                    continue  
                else:

                    bd1.cursor.execute("insert into organizadorpessoa(nome,contato,endereço) values(%s,%s,%s)",(nomeORGANIZADOR,contato,Endereço))
                    bd1.connection.commit()
                    
                    bd1.cursor.execute("insert into equipes(nomeequipe,toplaner,midlaner,jungler,atirador,suport,treinador) values(%s,%s,%s,%s,%s,%s,%s)",(nomeEquipe,topLaner,midLaner,jungle,atirador,suporte,nomeTreinador))
                    bd1.cursor.execute("select id_pessoa from organizadorpessoa WHERE NOME = %s", (nomeORGANIZADOR,))
                    id_pessoa = bd1.cursor.fetchall()[0]
                    bd1.cursor.execute("insert into pessoajuridica(id_pessoa,cnpj) values(%s,%s)", (id_pessoa,cnpj))
                    bd1.connection.commit()
                    print('Equipe cadastrada com sucesso.')
                    a = 1 
               

        
def registrarCampeonato():
    cls()
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
    
    vitoria = 0
    derrota = 0

    x = 0
    while x == 0:

        nomeDaEquipe = input('Insira o nome da equipe que você criou -> ')
        bd1.cursor.execute("select nomeequipe from equipes where nomeequipe = %s", (nomeDaEquipe,))
        bdEquipes = bd1.cursor.rowcount

        if bdEquipes > 0:
            bd1.cursor.execute("insert into campeonatos(cod_campeonato,nome,data_inicio,data_fim,categoria) values(%s,%s,%s,%s,%s)",(cod_Campeonato,nome_Campeonato,data_inicio,data_fim,categoria))
            bd1.connection.commit()
            bd1.cursor.execute(f"select cod_equipe from equipes where nomeequipe = '{nomeDaEquipe}'")
            codigoEquipeBD = bd1.cursor.fetchone()[0]
            bd1.cursor.execute(f"select cod_campeonato from campeonatos where cod_campeonato = {cod_Campeonato}")
            codcampeonato = bd1.cursor.fetchone()[0]
            bd1.cursor.execute("insert into timecampeonato(cod_campeonato, cod_equipe, vitorias, derrotas) values(%s,%s,%s,%s)", (codcampeonato,codigoEquipeBD,vitoria, derrota))
            bd1.connection.commit()

            print('Campeonato registrado.')
            x = 1
        else:
            print("Equipe inexistente, registre sua equipe primeiro e volte aqui.")
            x = 1
    
    print('Campeonato registrado.')

def JogosCAMPEONATOS():
    cls()
    cod_camps = int(input('Insira o código do campeonato -> '))

    bd1.cursor.execute("select cod_campeonato from campeonatos where cod_campeonato = %s", (cod_camps,))
    bdcod_camps = bd1.cursor.rowcount
    DATE = 0
    
    if bdcod_camps > 0:
        while DATE == 0:

            bd1.cursor.execute('select cod_campeonato from partidas where cod_campeonato = %s', (cod_camps,))
            EXISTENTE = bd1.cursor.rowcount

            if EXISTENTE == 0:
                data_inicio_partida = input('Insira a data de ínicio das partidas [dd/mm/yyyy] -> ')
                hora_partidas = input('Insira a hora de inicio das partidas [hh:mm] -> ')
                local_partidas = input('Insira o local dos partidas -> ')

                bd1.cursor.execute('select data_inicio from campeonatos where data_inicio = %s', (data_inicio_partida,))
                DATeBD = bd1.cursor.rowcount

                if DATeBD > 0:

                    bd1.cursor.execute('select cod_campeonato from campeonatos where cod_campeonato = %s', (cod_camps,))
                    cod_campsBD = bd1.cursor.fetchall()[0]

                    bd1.cursor.execute('insert into partidas(data_inicio_partidas, hora_partidas, local_partidas, cod_campeonato) values(%s,%s,%s,%s)', (data_inicio_partida, hora_partidas,local_partidas,cod_campsBD))
                    bd1.connection.commit()
                    print('Informações do campeonato atualizada.')
                    time.sleep(5)
                    DATE = 1
                else:
                    print('Data não encontrada neste campeonato.')
                    continue
            else:
                print('As informações desse campeonato já foram definidas.')
                time.sleep(10)
                DATE = 1
    else:
        print('Campeonato inexistente.')

def VerCamp():
    cls()
    cod_camps = int(input('Insira o código do campeonato -> '))

    bd1.cursor.execute("select cod_campeonato from campeonatos where cod_campeonato = %s", (cod_camps,))
    bdcod_camps = bd1.cursor.rowcount

    if bdcod_camps > 0:
        print('\nCampeonato ativo, segue as informacões ↯\n')
        bd1.cursor.execute(f"select * from campeonatos  where cod_campeonato = '{cod_camps}'")
        infoCamp = bd1.cursor.fetchall()[0]
        print(f'Código do campeonato -> {infoCamp[0]}\nNome do campeonato -> {infoCamp[1]}\nData de inicio -> {infoCamp[2]}\nData final -> {infoCamp[3]}\nCategoria -> {infoCamp[4]}\n')
        time.sleep(10)
    else:
        print('Campeonato inexistente.')


def VerEquipes():
    cls()

    nomeDaEquipe = input('Insira o nome da equipe -> ')

    bd1.cursor.execute(f"select nomeequipe from equipes where nomeequipe = '{nomeDaEquipe}'" )
    bdEquipes = bd1.cursor.rowcount

    if bdEquipes > 0:
        print('\nEquipe cadastrada, segue as informacões ↯\n')
        bd1.cursor.execute("select * from equipes where nomeequipe = %s", (nomeDaEquipe,))
        infoEquipes = bd1.cursor.fetchall()[0]
        print(f'Nome Da Equipe -> {infoEquipes[0]}\nCodigo da Equipe -> {infoEquipes[1]}\nTop Laner -> {infoEquipes[2]}\nJungler -> {infoEquipes[4]}\nMid Laner -> {infoEquipes[3]}\nAtirador -> {infoEquipes[5]}\nSuporte -> {infoEquipes[6]}\nReserva -> {infoEquipes[7]}\nTreinador -> {infoEquipes[8]}')
        time.sleep(10)
    else:
        print('Equipe inexistente.')


         
def Entrar():
    
    usuario = input('Úsuario: ')
    senha = input('Senha: ')
    pop = 0
    while pop == 0:

        bd1.cursor.execute("SELECT usuario,senha FROM usuarios WHERE usuario=%s AND senha=%s",(usuario, senha))
        numRow = bd1.cursor.rowcount
        
        if numRow == 1:
            #usuário logado

            cls()
            print('1 -> Registrar campeonato\n2 -> Ver campeonatos [ativos]\n3 -> Registrar Equipe\n4 -> Vincular telefone\n5 -> Infomações da conta\n6 -> Ver Equipes\n7 -> Adicionar informações do campeonato\n8 -> Sair')
            ops = int(input('Insira -> '))

            if ops == 7:
                JogosCAMPEONATOS()
                cls()
            if ops == 5:
                cls()
                print('\nSegue abaixo as informações da sua conta ↯\n')

                bd1.cursor.execute("select * from usuarios where usuario = %s",(usuario,))  
                infoCONTA = bd1.cursor.fetchall()[0]

                if infoCONTA[0] == 0: 
                    bd1.cursor.execute(f"select * from usuarios where usuario = '{usuario}'")
                    infoUSUARIO = bd1.cursor.fetchall()[0]
                    print(f'Telefone -> Sem registro\nEmail -> {infoUSUARIO[2]}\nNick -> {infoUSUARIO[3]}\nUsuario -> {infoUSUARIO[4]}\nSenha -> ******\nData nascimento -> {infoUSUARIO[6]}')
                    time.sleep(20)
                else:
                    bd1.cursor.execute(f"select * from usuarios where usuario = '{usuario}'")
                    infoUSUARIO = bd1.cursor.fetchall()[0]
                    print(f'Telefone -> {infoUSUARIO[0]}\nEmail -> {infoUSUARIO[2]}\nNick -> {infoUSUARIO[3]}\nUsuario -> {infoUSUARIO[4]}\nSenha -> ******\nData nascimento -> {infoUSUARIO[6]}')
                    time.sleep(20)
                cls()
            if ops == 6:
                VerEquipes()
                cls()
            if ops == 4:
                back = 0
                
                while back == 0:
                    tel = input('Digite o número [+DDD][8212345678] -> +')
                    
                    if len(tel) > 13:
                        print('Número passou do limite [13 Números]')
                        continue

                    if tel.isnumeric() == True: 
                        bd1.cursor.execute("select telefone from usuarios where usuario = %s",(usuario,))  
                        pegar = bd1.cursor.fetchone()[0]
                        print(str(pegar))
                        if pegar == '0':
                            bd1.cursor.execute("update usuarios set telefone = %s where usuario = %s",(tel,usuario))
                            bd1.connection.commit()
                            print('Vinculado com sucesso')
                            back = 1
                            
                        else:
                            bd1.cursor.execute("select telefone from usuarios where usuario = %s",(usuario,))  
                            bdTelefone = bd1.cursor.fetchall()
                            
                            print(f'Conta já vinculada com telefone {bdTelefone[0]}') 
                            back = 1                 
                    else:
                        print('Apenas números!')
                        continue
            if ops == 1:
                registrarCampeonato()
                cls()
            if ops == 2:
                VerCamp()
                cls()
            if ops == 3:
                registrarEquipes()
                cls()
            if ops == 8:
                print('Deslogado.')
                time.sleep(2.5)
                break
        else:
            print("Usuário ou senha incorretos!\n")
            pop = 1

cls()
conti = 0
while conti == 0:
    print('1 -> Entrar\n2 -> Criar Conta')
    opc = int(input('Insira -> '))

    if opc == 2:
        criarconta()

    elif opc == 1:
        Entrar()
     
        

 
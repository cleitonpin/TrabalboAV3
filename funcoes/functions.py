from funcoes import bd1
import random
import time
import os 
from datetime import datetime
import hashlib
import sys
from funcoes import data, email, usuario, criador_de_conta, functions
from cassiopeia import Champion, Champions
import cassiopeia as cass
from funcoes import bd1
from validador import email, usuario, data
from utils.senha import gerador

    
cass.set_riot_api_key("RGAPI-ac923fc3-6bfd-430b-b693-639e0d1dbc53")  # This overrides the value set in your configuration/settings.
cass.set_default_region("BR")


#cores 
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# menu
def menu():
    print(color.RED+"#"*53+color.END)
    print(color.RED+"#                                                   #"+color.END)
    print(color.RED+"#"+color.END+color.DARKCYAN+"                      RifsPopo                     "+color.END+color.RED+"#"+color.END)
    print(color.RED+"#                                                   #"+color.END)
    print(color.RED+"#"*53+color.END)
#função limpar tela
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
#função mudar nick
def mudarNICK(nick, usuario):
    #selecionando o nick e usuarios para verificação
    bd1.cursor.execute("select nick, usuario from usuarios where nick = %s and usuario = %s", (nick,usuario))
    countNICK = bd1.cursor.rowcount
    N = 0
    #verificando de nick e usuario digitado existeno bd
    while N == 0:
        if countNICK > 0:
            newNICK = input('Insira seu novo nick -> ')
            #mudando o nick ja existente
            bd1.cursor.execute('update usuarios set nick = %s where usuario = %s', (newNICK,usuario))
            bd1.connection.commit()
            print('Nick mudado com sucesso!')
            time.sleep(5)
            N = 1
            cls()
        else:
            print('Nick ou úsuario não encontrados.')
            time.sleep(3)
            N = 1
            cls()
def VerCamp(cod_camps):
    cls()
    
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

def get_champions():
   # champions = Champions(region='BR')

   # for champion in champions:
   #       print(champion.name, champion.id)

    cls()

    camp = input('Insira o nome do campeão -> ')
    # annie = Champion(name="Annie", region="NA")
    annie = Champion(name=camp, region="BR")

    
    
    print(f"""
Campeão: {annie.name}

Dano de ataque: {annie.stats.attack_damage} (+{annie.stats.attack_damage_per_level} por nível)
Vida: {annie.stats.health} (+{annie.stats.health_per_level} por nível)
Mana: {annie.stats.mana} (+{annie.stats.mana_per_level} por nível)
Armadura: {annie.stats.armor} (+{annie.stats.armor_per_level} por nível)
Resistência mágica: {annie.stats.magic_resist} (+{annie.stats.magic_resist_per_level} por nível) 

""")

    null = input('aperte enter para contiuar')

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
                verificarData = data_inicio_partida.find('/')

                if verificarData == -1:
                    cls()
                    print(f'ERROR: FORMATO DA DATA INVÁLIDO. ausência de "/" [{data_inicio_partida}]')
                    time.sleep(5)
                    continue
                bd1.cursor.execute('select data_inicio from campeonatos where data_inicio = %s', (data_inicio_partida,))
                DATeBD = bd1.cursor.rowcount

                if DATeBD > 0:

                    bd1.cursor.execute('select cod_campeonato from campeonatos where cod_campeonato = %s', (cod_camps,))
                    cod_campsBD = bd1.cursor.fetchall()[0]

                    bd1.cursor.execute('insert into partidas(data_inicis_partidas, hora_partidas, local_partidas, cod_campeonato) values(%s,%s,%s,%s)', (data_inicio_partida, hora_partidas,local_partidas,cod_campsBD))
                    bd1.connection.commit()
                    print('Informações das partidas do campeonato atualizada.')
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
    DATA  = 0
    while DATA == 0:

        nome_Campeonato = input('Insira o nome do campeonato -> ')
        data_inicio = input('Insira a data de ínicio [dd/mm/yyyy] -> ')
        data_fim = input('Insira a data final [dd/mm/yyyy] -> ')
        categoria = input('Insira a categoria -> ')

        verificarData = (data_inicio.find('/'),data_fim.find('/'))

        if len(data_inicio) < 10:
            if verificarData[0] == -1:
                cls()
                print(f'ERROR: FORMATO INVÁLIDO. [{data_inicio}]')
                time.sleep(5)
                continue
        if len(data_fim) < 10:
            if verificarData[1] == -1:
                cls()
                print(f'ERROR: FORMATO INVÁLIDO. [{data_fim}]')
                time.sleep(5)
                continue



        date = datetime.strptime(data_inicio, '%d/%m/%Y')
        date2 = datetime.strptime(data_fim, '%d/%m/%Y')
        data_Atual = date.today()

        if date >= date2:
            cls()
            print('ERROR: FORMATO DA DATA INSERIDA INVÁLIDA')
            time.sleep(5)
            continue

        if date <= data_Atual or date2 <= data_Atual:
            cls()
            print('ERROR: FORMATO DA DATA INSERIDA INVÁLIDA')
            time.sleep(5)
            continue
        
 
    
        bd1.cursor.execute("insert into campeonatos(cod_campeonato,nome,data_inicio,data_fim,categoria) values(%s,%s,%s,%s,%s)",(cod_Campeonato,nome_Campeonato,data_inicio,data_fim,categoria))
        bd1.connection.commit()

        print('Campeonato registrado.')
        DATA = 1
        time.sleep(2)
        
def registrarEquipes():
    cls()
    global nomeDaEquipe

    a = 0 

    while a == 0:

        nomeORGANIZADOR = input('Insira seu nome pessoal -> ')
        Endereço = input('Insira seu endereço -> ') 
        contato = _valida_email()
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
                    time.sleep(2)
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

def VerEquipes(nomeDaEquipe):
    cls()
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
def check_login():
    usuario = input('Úsuario: ')
    senha = input('Senha: ')
    senha2 = hashlib.md5(str(senha).encode('utf-8')).hexdigest()
    pop  = 0
    while pop == 0:
        

        bd1.cursor.execute("SELECT usuario,senha FROM usuarios WHERE usuario=%s AND senha=%s",(usuario, senha2))
        numRow = bd1.cursor.rowcount
        
        if numRow == 1:
            #usuário logado
            cls()
            menu()
            print(color.RED+'1 -> Registrar campeonato\n2 -> Ver campeonatos [ativos]\n3 -> Registrar Equipe\n4 -> Infomações da conta\n5 -> Ver Equipes\n6 -> Adicionar informações das partidas no campeonato\n7 -> Configurações da conta\n0 -> Sair')
            opc1 = int(input('Insira -> '))

            if opc1 == 6:
                functions.JogosCAMPEONATOS()
                cls()
                continue
            elif opc1 == 4:
                cls()
                print('\nSegue abaixo as informações da sua conta ↯\n')

                bd1.cursor.execute("select * from usuarios where usuario = %s",(usuario,))  
                infoCONTA = bd1.cursor.fetchall()[0]

                if infoCONTA[0] == 0: 
                    bd1.cursor.execute(f"select * from usuarios where usuario = '{usuario}'")
                    infoUSUARIO = bd1.cursor.fetchall()[0]
                    print(f'Telefone -> Sem registro\nEmail -> {infoUSUARIO[2]}\nNick -> {infoUSUARIO[3]}\nUsuario -> {infoUSUARIO[4]}\nSenha -> {infoUSUARIO[5]}\nData nascimento -> {infoUSUARIO[6]}')
                    time.sleep(20)
                else:
                    bd1.cursor.execute(f"select * from usuarios where usuario = '{usuario}'")
                    infoUSUARIO = bd1.cursor.fetchall()[0]
                    print(f'Telefone -> {infoUSUARIO[0]}\nEmail -> {infoUSUARIO[2]}\nNick -> {infoUSUARIO[3]}\nUsuario -> {infoUSUARIO[4]}\nSenha -> {infoUSUARIO[5]}\nData nascimento -> {infoUSUARIO[6]}')
                    time.sleep(20)
                cls()
                continue
            elif opc1 == 5:
                functions.VerEquipes(nomeDaEquipe = input('Insira o nome da equipe -> '))
                cls()
                continue
            elif opc1 == 1:
                functions.registrarCampeonato()
                cls()
                continue
            elif opc1 == 2:
                functions.VerCamp(cod_camps  = int(input('Insira o código do campeonato -> ')))
                cls()
                continue
            elif opc1 == 3:
                functions.registrarEquipes() 
                cls()
                continue
            elif opc1 == 0:
                cls()
                print('Deslogado.')
                time.sleep(2.5)
                break
            elif opc1 == 7:
                cls()
                configs(opc1)
                cls()
                continue
            else:
                print('Digite corretamente!')
                time.sleep(2.5)
                continue   
                cls()
                
        else:
            cls()
            print("Usuário ou senha incorretos!\n") 
            time.sleep(3)     
            pop = 1
    cls()   

def mudarSENHA(usuario, senha):

    C = True

    while C == True:

        bd1.cursor.execute("select senha, usuario from usuarios where senha = %s and usuario = %s", (senha,usuario))
        countpassw = bd1.cursor.rowcount

        if countpassw > 0:
            newSENHA = input('Insira sua nova senha -> ')
            senhaCRYPTED = hashlib.md5(str(newSENHA).encode('utf-8')).hexdigest()
            bd1.cursor.execute('update usuarios set senha = %s where usuario = %s', (senhaCRYPTED,usuario))
            bd1.connection.commit()
            print('Senha mudada com sucesso!')
            time.sleep(1.5)
            C = False
            cls()
        else:
            print('Senha ou úsuario digitados incorretos!')
            continue
            cls()
            
def mudaremail(usuario, email):
    C = True

    while C == True:

        bd1.cursor.execute("select senha, usuario from usuarios where email = %s and usuario = %s", (email,usuario))
        countemail = bd1.cursor.rowcount

        if countemail > 0:
            newEmail = input('Insira seu novo email -> ')
            bd1.cursor.execute('update usuarios set email = %s where usuario = %s', (newEmail,usuario))
            bd1.connection.commit()
            print('Email mudado com sucesso!')
            time.sleep(1.5)
            C = False
            cls()
        else:
            print('Email ou úsuario digitados incorretos!')
            continue
            cls()

def configs(opc1):
    
    cf = True
    while cf == True:
        print('1 -> Mudar Nick\n2 -> Mudar senha\n3 -> Mudar nome de úsuario\n4 -> Mudar email\n5 -> Vincular telefone\n0 -> Voltar')    
        config = int(input('Insira [1-5]-> '))
        if config == 5:
            x = True         
            while x == True:
                
                user = True
                while user == True:
                    usuario = input('Digite seu úsuario -> ')
                    bd1.cursor.execute("select usuario from usuarios where usuario = %s",(usuario,)) 
                    use = bd1.cursor.rowcount

                    if use > 0:
                        user = False
                    else:
                        print("Úsuario digitado não encontrado")
                        user = True
                tel = input('Digite o número [+DD][8212345678] -> +')
                                        
                if len(tel) > 13:
                    print('Número passou do limite [13 Números]')
                    continue

                if tel.isnumeric() == True: 

                    bd1.cursor.execute("select telefone from usuarios where usuario = %s",(usuario,))  
                    pegar = bd1.cursor.fetchone()[0]
                    #print(str(pegar))
                    if str(pegar) == '0':
                        bd1.cursor.execute("update usuarios set telefone = %s where usuario = %s",(tel,usuario))
                        bd1.connection.commit()
                        print('Vinculado com sucesso')
                        cls()
                        x = False             
                    else:
                        bd1.cursor.execute("select telefone from usuarios where usuario = %s",(usuario,))  
                        bdTelefone = bd1.cursor.fetchall()
                                                
                        print(f'Conta já vinculada com telefone {bdTelefone[0]}') 
                        cls()
                        x = False                
                else:
                    print('Apenas números')
                    continue
        elif config == 1:
            cls()
            mudarNICK(input('Insira seu nick atual -> '), input('Insira seu úsuario -> '))
        elif config == 0:
            cf = False
        elif config == 2:
            senha = input('Insira sua senha atual: ')
            senha2 = hashlib.md5(str(senha).encode('utf-8')).hexdigest()
            mudarSENHA(input('Insira seu nome de úsuario -> '), senha2)
            cls()
        elif config == 4:
            mudaremail(input('Insira seu nome de úsuario -> '), input('Insira seu email atual -> '))


"""trabson.py"""
# -*- utf-8 -*-

# import hashlib
# import datetime

def _encerra_programa():

    opcao = input('Deseja criar novamente, s ou n? ')

    if opcao == 'n':
        return 0
    return 1


def _valida_usuario():
    """_valida_usuario"""

    usuario_input = ''

    while True:
        usuario_input = input('Insira seu usuario -> ')

        if usuario.valida(usuario_input):
            break
        print('Usuário invalido')
    return usuario_input


def _gera_senha():

    return gerador.gera(input('Insira sua senha -> '))


def _valida_email():

    email_input = ''

    while True:

        email_input = input('Insira um e-mail válido -> ')

        if email.valida(email_input):
            break
        print('email inválido')
    return email_input


def _valida_data():

    data_nascimento = 0

    while True:
        data_nascimento = input(
            'Insira sua data de nascimento [+14] [dd/mm/yyyy] -> ')

        if data.valida(data_nascimento):
            break
        print('Data inválida')

    return data_nascimento


def cria():
    """cria"""
    
    continua = 1
    while continua == 1:

        telefone = 0

        usuario = _valida_usuario()
        senha = _gera_senha()
        email = _valida_email()
        data = _valida_data()
        nick = input('Insira seu nick -> ')
        jogador = """
            Jogador 01
            Nome: {USUARIO},
            E-mail: {EMAIL},
            Senha: {SENHA}
            Data: {DATA}
            Nick: {NICK}
        """.format(USUARIO=usuario, SENHA=senha, EMAIL=email, DATA=data, NICK=nick)

        bd1.cursor.execute("select usuario from usuarios where usuario = %s", (usuario,))
        rowUsuario = bd1.cursor.rowcount 
        bd1.cursor.execute("select nick from usuarios where nick = %s", (nick,))
        rowNick = bd1.cursor.rowcount 

        row= (rowUsuario, rowNick)
        if row[0] > 0 or row[1] > 0:
            if row[0] > 0:
                cls()
                print('ERROR: Usuário já existe')
            if row[1] > 0:
                cls()
                print('ERROR: Nick já existe')      
        else: 
            bd1.cursor.execute("insert into usuarios(telefone,email,usuario,nick,datanasc,senha) values(%s,%s,%s,%s,%s,%s)",(telefone,email,usuario,nick,data,senha))
            bd1.connection.commit()
            cls()
            print('Úsuario cadastrado com sucesso')
            time.sleep(5)
        print(jogador)

        continua = _encerra_programa()


#        nick = input('Insira seu nick: ')
#
#        str_date = '01/01/2005'
#        date = datetime.strptime(str_date, '%d/%m/%Y')
#        date2 = datetime.strptime(data, '%d/%m/%Y')
#        if date2 > date:
#            print('Apenas maiores de 14 anos.')
#            time.sleep(5)
#            continue
#
#        bd1.cursor.execute(
#            "select usuario from usuarios where usuario = %s", (usuario,)
#        )
#        rowUsuario = bd1.cursor.rowcount
#        bd1.cursor.execute(
#            "select nick from usuarios where nick = %s", (nick,)
#        )
#        rowNick = bd1.cursor.rowcount
#
#        row= (rowUsuario, rowNick)
#        if row[0] > 0 or row[1] > 0:
#            if row[0] > 0:
#                print('ERROR: Usuário já existe')
#            if row[1] > 0:
#                print('ERROR: Nick já existe')
#        else:
#            bd1.cursor.execute(
#                "insert into usuarios(
#                    telefone,email,usuario,nick,data,senha)
#                values(%s,%s,%s,%s,%s,%s)"
#            ,(telefone,email,usuario,nick,data,senha))
#            bd1.connection.commit(
#            print('Úsuario cadastrado com sucesso')
#            time.sleep(5)
#            continua = 0

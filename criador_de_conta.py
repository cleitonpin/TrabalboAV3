"""trabson.py"""
# -*- utf-8 -*-

# import hashlib
# import datetime
# import time
from validador import data


def cria():
    """cria"""

    continua = 1
    while continua == 1:

        # telefone = 0

        data_nascimento = 0
        data_valida = True

        while data_valida:
            data_nascimento = input(
                'Insira sua data de nascimento [+14] [dd/mm/yyyy]: ')

            if not data.valida(data_nascimento):
                print('Data inválida')
            else:
                data_valida = False

        opcao = input('Deseja continuar, s ou n? ')
        if opcao == 'n':
            continua = 0


#        usuario = input('Insira seu usuario: ')
#        senha = input('Insira sua senha: ')
#        email = input('Insira um e-mail válido: ')
#        nick = input('Insira seu nick: ')
#
#        hash = hashlib.md5(str(senha).encode('utf-8'))
#        senhaMD5 = hash.hexdigest()
#
#        verificaremail = (email.find('@'),email.find('.com'))
#
#        str_date = '01/01/2005'
#        date = datetime.strptime(str_date, '%d/%m/%Y')
#        date2 = datetime.strptime(data, '%d/%m/%Y')
#        if date2 > date:
#            print('Apenas maiores de 14 anos.')
#            time.sleep(5)
#            continue
#        if verificaremail[0] == -1:
#            print("Erro: email inválido [ausência de: '@']\n")
#            time.sleep(5)
#            continue
#        if verificaremail[1] == -1:
#            print("Erro: email inválido [ausência de: '.com/.com.br/...']\n")
#            time.sleep(5)
#            continue
#        if len(usuario) < 4:
#            print('Número de caracteres insuficiente[mínimo 4]\n')
#            time.sleep(5)
#            continue
#        elif len(usuario) > 12:
#            print('Número de caracteres acima do indicado[máximo de 12]\n')
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

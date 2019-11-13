"""trabson.py"""
# -*- utf-8 -*-

# import hashlib
# import datetime
# import time
from validador import email, usuario, data


def _encerra_programa():

    opcao = input('Deseja continuar, s ou n? ')

    if opcao == 'n':
        return 0
    return 1


def _valida_usuario():
    """_valida_usuario"""

    usuario_input = ''

    while True:
        usuario_input = input('Insira seu usuario: ')

        if usuario.valida(usuario_input):
            return False
        print('Usuário invalido')
    return usuario_input


def _valida_email():

    email_input = ''

    while True:

        email_input = input('Insira um e-mail válido: ')

        if email.valida(email_input):
            return False
        print('email inválido')
    return email_input


def _valida_data():

    data_nascimento = 0

    while True:
        data_nascimento = input(
            'Insira sua data de nascimento [+14] [dd/mm/yyyy]: ')

        if data.valida(data_nascimento):
            return False
        print('Data inválida')

    return data_nascimento


def cria():
    """cria"""

    continua = 1
    while continua == 1:

        # telefone = 0

        #
        #        senha = gerador.gera(input('Insira sua senha: '))
        #

        # usuario = _valida_usuario()
        # email = _valida_email()
        # _valida_data()
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

from funcoes import bd1
import time
import os
import hashlib

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def mudarNICK(nick,usuario):
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
            print('Senha ou úsuariodigitados incorretos!')
            cls()
            continue
            
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
            cls()
            continue
 

def esquecisenha(usuario, email):
    bd1.cursor.execute(f"SELECT usuario,senha,email FROM usuarios WHERE usuario = '{usuario}' AND email = '{email}'")
    row = bd1.cursor.rowcount
     
    c = True
    while c == True:

        if row > 0:
        
            try:

                newSENHA = input('Insira sua nova senha -> ')
                senhaCRYPTED = hashlib.md5(str(newSENHA).encode('utf-8')).hexdigest()
                bd1.cursor.execute('update usuarios set senha = %s where usuario = %s', (senhaCRYPTED,usuario))
                bd1.connection.commit()
                print('Senha mudada com sucesso!')
                time.sleep(1.5)
                c = False
            except:
                cls()
                continue
        else:
            print("Úsuario ou email digitados não encontrados")
            time.sleep(1)
            cls()
            c = False

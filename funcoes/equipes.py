from funcoes import bd1, functions
import time

def change_team(equipe):


    bd1.cursor.execute(f"SELECT nomeequipe FROM equipes WHERE nomeequipe = '{equipe}'")
    row = bd1.cursor.rowcount

    if row > 0:
        newNameteam = input("Insira o novo nome da equipe -> ")
        bd1.cursor.execute(f"UPDATE equipes set nomeequipe = '{newNameteam}' WHERE nomeequipe = '{equipe}'")
        bd1.connection.commit()
        print('Nome da equipe alterada.')
        time.sleep(1.5)
    else:
        print('Nome da equipe não encontrada')
        time.sleep(2)

def change_top(top):

    bd1.cursor.execute(f"SELECT toplaner FROM equipes WHERE toplaner = '{top}'")
    row1 = bd1.cursor.rowcount

    if row1 > 0:
        newNametop = input("Insira o nome do novo jogador do top -> ")
        bd1.cursor.execute(f"UPDATE equipes set toplaner = '{newNametop}' WHERE toplaner = '{top}'")
        bd1.connection.commit()
        print('Jogador do top alterado.')
        time.sleep(1.5)
    else:
        print('Jogador não encontrado')
        time.sleep(1.5)

def change_mid(mid):

    bd1.cursor.execute(f"SELECT midlaner FROM equipes WHERE midlaner = '{mid}'")
    row2 = bd1.cursor.rowcount

    if row2 > 0:
        newNamemid = input("Insira o nome do novo jogador da mid laner -> ")
        bd1.cursor.execute(f"UPDATE equipes set midlaner = '{newNamemid}' WHERE toplaner = '{mid}'")
        bd1.connection.commit()
        print('Jogador do mid alterado.')
        time.sleep(1.5)
    else:
        print('Jogador não encontrado')
        time.sleep(1.5)

def change_jungle(jungle):

    bd1.cursor.execute(f"SELECT jungler FROM equipes WHERE jungler = '{jungle}'")
    row3 = bd1.cursor.rowcount

    if row3 > 0:
        newNamejungle = input("Insira o nome do novo jogador da jungle -> ")
        bd1.cursor.execute(f"UPDATE equipes set jungler = '{newNamejungle}' WHERE jungler = '{jungle}'")
        bd1.connection.commit()
        print('Jogador da jungle alterado.')
        time.sleep(1.5)
    else:
        print('Jogador não encontrado')
        time.sleep(1.5)

def change_adc(adc):

    bd1.cursor.execute(f"SELECT atirador FROM equipes WHERE atirador = '{adc}'")
    row4 = bd1.cursor.rowcount

    if row4 > 0:
        newNameadc = input("Insira o nome do novo atirador -> ")
        bd1.cursor.execute(f"UPDATE equipes set midlaner = '{newNameadc}' WHERE atirador = '{adc}'")
        bd1.connection.commit()
        print('Nome do atirador alterado.')
        time.sleep(1.5)
    else:
        print('Jogador não encontrado')
        time.sleep(1.5)
    
def change_sup(sup):

    bd1.cursor.execute(f"SELECT suport FROM equipes WHERE suport = '{sup}'")
    row5 = bd1.cursor.rowcount

    if row5 > 0:
        newNamesup = input("Insira o nome do novo suporte -> ")
        bd1.cursor.execute(f"UPDATE equipes set midlaner = '{newNamesup}' WHERE suport = '{sup}'")
        bd1.connection.commit()
        print('Nome do suporte alterado.')
        time.sleep(1.5)
    else:
        print('Jogador não encontrado')
        time.sleep(1.5)

def reserva(equipe):

    bd1.cursor.execute(f"select reservas from equipes where nomeequipe = '{equipe}'")
    cont = bd1.cursor.fetchone()[0]

    if cont == None:
        newReserva= input("Insira o nome do novo reserva -> ")
        bd1.cursor.execute(f"UPDATE equipes set reservas = '{newReserva}' WHERE nomeequipe = '{equipe}'")
        bd1.connection.commit()
        print('Reserva adicionado.')
        time.sleep(1.5)
    else:
        print("Já tem reserva, pode apenas 1")
        time.sleep(1)
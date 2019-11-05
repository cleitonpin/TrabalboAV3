import bd1
import random
import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

cls()


equipes = [[], [], [], [], [], [], [], []]

qntdEquipe = int(input('Digite quantas equipes irá inscrever-se para o preenchimento manual -> '))
resto = 8 - qntdEquipe

for n in range(qntdEquipe):
    equipes[n].append(input(f'Digite o nome da equipe {n}ª -> '))
   
print('\n')

for n in range(resto):
    resto += 1
    equipes[resto].append(input("Digite -> "))
    

print(f'Quartas de finais\n{equipes[0]} vs {equipes[1]}\n{equipes[2]} vs {equipes[3]}\n{equipes[4]} vs {equipes[5]}\n{equipes[6]} vs {equipes[7]}') 





# for n in range(qntdEquipe):

#     a = 0
#     while a == 0:

#         nomeORGANIZADOR = input('Insira seu nome pessoal -> ')
#         Endereço = input('Insira seu endereço -> ') 
#         contato = input('Insira seu email (válido) para contato -> ')
#         pessoa = int(input('Cadastrar a equipe como: Pessoa Física [1] ou Juridíca [2] -> '))

#         verificaremail = (contato.find('@'),contato.find('.com'))

#         if verificaremail[0] == -1:
#             print("\n\nErro: email inválido [ausência de: '@']\n")
#             continue
#         if verificaremail[1] == -1:
#             print("\n\nErro: email inválido [ausência de: '.com/.com.br/...']\n")
#             continue

#         if pessoa == 1:
                
#             nomeEquipe = input('Insira o nome da equipe que deseja inscrever no campeonato -> ')
#             equipes.append(nomeEquipe)
#             nomeDaEquipe = nomeEquipe
#             nomeTreinador = input('Insira o nome do treinador -> ')
#             topLaner = input('\nExemplo nome -> Flavio "Jukes" Fernandes\n\nNome do top laner [Nome "Nick" Sobrenome] -> ')
#             jungle = input('Nome do jungle [Nome "Nick" Sobrenome] -> ')
#             midLaner = input('Nome do mid laner [Nome "Nick" Sobrenome] -> ')
#             atirador = input('Nome do atirador [Nome "Nick" Sobrenome] -> ')
#             suporte = input('Nome do suporte [Nome "Nick" Sobrenome] -> ')
#             reserva = input('Há reservas s/n? ')

#             if reserva == 's':
#                 print('Pode apenas 1 reserva\n')
#                 nomeReserva = input('Insira o nome e a lane [Flavio "Jukes" Fernandes]-[TopLaner] -> ')      
                    
#                 cpf = input('Insira seu cpf (XXX.XXX.XXX-XX) -> ')
                    
#                 if len(cpf) > 11 or len(cpf) < 11:
#                     print ('Valores inseridos esta fora do padrão, por favor tente novamente.')
#                     continue  
#                 else:

#                     bd1.cursor.execute("insert into organizadorpessoa(nome,contato,endereço) values(%s,%s,%s)",(nomeORGANIZADOR,contato,Endereço))
#                     bd1.connection.commit()

#                     bd1.cursor.execute("insert into equipes(nomeequipe,toplaner,midlaner,jungler,atirador,suport,treinador,reservas) values(%s,%s,%s,%s,%s,%s,%s,%s)",(nomeEquipe,topLaner,midLaner,jungle,atirador,suporte,nomeTreinador,nomeReserva))                
#                     bd1.cursor.execute("select id_pessoa from organizadorpessoa WHERE NOME = %s", (nomeORGANIZADOR,))
#                     id_pessoa = bd1.cursor.fetchall()
    
#                     bd1.cursor.execute("insert into pessoafisica(id_pessoa,cpf) values(%s,%s)", (id_pessoa[0],cpf))
#                     bd1.connection.commit()
#                     print('Equipe cadastrada com sucesso.')
#                     a = 1 
#             else:
#                 cpf = input('Insira seu cpf (XXX.XXX.XXX-XX) -> ')
                    
#                 if len(cpf) > 11 or len(cpf) < 11:
#                     print ('Valores inseridos esta fora do padrão, por favor tente novamente.')
#                     continue  
#                 else:                                  
#                     bd1.cursor.execute("insert into organizadorpessoa(nome,contato,endereço) values(%s,%s,%s)",(nomeORGANIZADOR,contato,Endereço))
#                     bd1.connection.commit()
#                     bd1.cursor.execute("insert into equipes(nomeequipe,toplaner,midlaner,jungler,atirador,suport,treinador) values(%s,%s,%s,%s,%s,%s,%s)",(nomeEquipe,topLaner,midLaner,jungle,atirador,suporte,nomeTreinador))                
#                     bd1.cursor.execute("select id_pessoa from organizadorpessoa WHERE NOME = %s", (nomeORGANIZADOR,))
#                     id_pessoa = bd1.cursor.fetchall()
    
#                     bd1.cursor.execute("insert into pessoafisica(id_pessoa,cpf) values(%s,%s)", (id_pessoa[0],cpf))
#                     bd1.connection.commit()
#                     print('Equipe cadastrada com sucesso.')
#                     a = 1 
                    
#         else:


#             nomeEquipe = input('Insira o nome da equipe que deseja inscrever no campeonato -> ')
#             equipes.append(nomeEquipe)
#             nomeTreinador = input('Insira o nome do treinador -> ')
#             topLaner = input('\nExemplo nome -> Flavio "Jukes" Fernandes\n\nNome do top laner [Nome "Nick" Sobrenome] -> ')
#             jungle = input('Nome do jungle [Nome "Nick" Sobrenome] -> ')
#             midLaner = input('Nome do mid laner [Nome "Nick" Sobrenome] -> ')
#             atirador = input('Nome do atirador [Nome "Nick" Sobrenome] -> ')
#             suporte = input('Nome do suporte [Nome "Nick" Sobrenome] -> ')
#             reserva = input('Há reservas s/n? ')

#             if reserva == 's':
#                 print('\nPode apenas 1 reserva\n')
#                 nomeReserva = input('Insira o nome e a lane [Flavio "Jukes" Fernandes][TopLaner] -> ')      
                    
#                 cnpj = input('Insira seu CNPJ (XX.XXX.XXX/XXXX.XX) -> ')
                    
#                 if len(cnpj) > 14 or len(cnpj) < 14:
#                     print ('Valores inseridos esta fora do padrão, por favor tente novamente.')
#                     continue  
#                 else:
                        
#                         #pegando foreign key

#                     bd1.cursor.execute("insert into organizadorpessoa(nome,contato,endereço) values(%s,%s,%s)",(nomeORGANIZADOR,contato,Endereço))
#                     bd1.connection.commit()
                        
#                     bd1.cursor.execute("insert into equipes(nomeequipe,toplaner,midlaner,jungler,atirador,suport,treinador,reservas) values(%s,%s,%s,%s,%s,%s,%s,%s)",(nomeEquipe,topLaner,midLaner,jungle,atirador,suporte,nomeTreinador,nomeReserva))
#                     bd1.cursor.execute("select id_pessoa from organizadorpessoa WHERE NOME = %s", (nomeORGANIZADOR,))
#                     id_pessoa = bd1.cursor.fetchall()[0]
#                     bd1.cursor.execute("insert into pessoajuridica(id_pessoa,cnpj) values(%s,%s)", (id_pessoa,cnpj))
#                     bd1.connection.commit()
#                     print('Equipe cadastrada com sucesso.')
#                     a = 1 
#             else:
#                 CJ =
#                 while
#                 cnpj = input('Insira seu CNPJ (XX.XXX.XXX/XXXX.XX) -> ')
                    
#                 if len(cnpj) > 14 or len(cnpj) < 14:
#                     print ('Valores inseridos esta fora do padrão, por favor tente novamente.')
#                     continue  
#                 else:

#                     bd1.cursor.execute("insert into organizadorpessoa(nome,contato,endereço) values(%s,%s,%s)",(nomeORGANIZADOR,contato,Endereço))
#                     bd1.connection.commit()
                        
#                     bd1.cursor.execute("insert into equipes(nomeequipe,toplaner,midlaner,jungler,atirador,suport,treinador) values(%s,%s,%s,%s,%s,%s,%s)",(nomeEquipe,topLaner,midLaner,jungle,atirador,suporte,nomeTreinador))
#                     bd1.cursor.execute("select id_pessoa from organizadorpessoa WHERE NOME = %s", (nomeORGANIZADOR,))
#                     id_pessoa = bd1.cursor.fetchall()[0]
#                     bd1.cursor.execute("insert into pessoajuridica(id_pessoa,cnpj) values(%s,%s)", (id_pessoa,cnpj))
#                     bd1.connection.commit()
#                     print('Equipe cadastrada com sucesso.')
#                     a = 1 




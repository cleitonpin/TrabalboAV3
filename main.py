import os 
from funcoes import functions, conta
import time
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

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')
 
cls()
conti = 0
while conti == 0:
    print(color.RED+"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                         #
#       Não tem uma conta? Crie agora, basta digitar 2    #
#                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
1 -> Entrar
2 -> Criar Conta
3 -> Esqueci senha
0 -> Encerrar programa
""")

    try:
        
        opc = int(input('Insira -> '))

        if opc == 2:
            functions.cria()

        elif opc == 3:
            conta.esquecisenha(input('Insira seu úsuario -> '),input('Insira seu email -> ') )
        elif opc == 0:
            conti = 1
        elif opc == 1:
            functions.check_login()
    except:
        print('Digite corretamente.')
        time.sleep(1)
        cls()
        continue
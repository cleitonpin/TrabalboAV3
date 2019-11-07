


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


lista = [[color.RED], [color.CYAN], [color.DARKCYAN], [color.END], [color.YELLOW], [color.UNDERLINE], [color.BOLD], [color.PURPLE]]
conti = 0
while conti == 0:
    
    print(color.PURPLE+"""
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #                                                         #
    #       Não tem uma conta? Crie agora, basta digitar 2    #
    #                                                         #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
    1 -> Entrar
    2 -> Criar Conta
    """)
    opc = int(input('    Insira -> '))
   
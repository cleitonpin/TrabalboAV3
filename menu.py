def show(color):
    """Mostra o menu
    """
    mensagem = color.DARKCYAN + 'Não tem uma conta? Crie agora, basta digitar 2'
    espaco = int(((80 - len(mensagem)) / 2)  + 2)
    cor_vermelha = color.RED
    jogo_da_velha = "#"

    linha_de_fora = cor_vermelha + jogo_da_velha * 80
    linha_interna = cor_vermelha + jogo_da_velha + " " * 78 + jogo_da_velha
    linha_do_meio = "{COR}{JOGO_DA_VELHA}{ESPACO}{MENSAGEM}{ESPACO}{COR}{JOGO_DA_VELHA}".format(
        COR = cor_vermelha,
        JOGO_DA_VELHA = jogo_da_velha,
        ESPACO = " "* espaco,
        MENSAGEM = mensagem
    )
    
    print("""
        {LINHA_DE_FORA}
        {LINHA_INTERNA}
        {LINHA_DO_MEIO}
        {LINHA_INTERNA}
        {LINHA_DE_FORA}
    """.format(
        LINHA_DE_FORA = linha_de_fora,
        LINHA_INTERNA = linha_interna,
        LINHA_DO_MEIO = linha_do_meio
        )
    )

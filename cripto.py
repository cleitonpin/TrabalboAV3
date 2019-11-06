# from cryptography.fernet import Fernet


# senha2 = bytes(input('Digite a senha ->'))
# senha = Fernet.generate_key()
# seila = Fernet(senha)
# texto = seila.encrypt(b"Uma mensagem secreta. Not for prying eyes.")
# print(texto)
# test = seila.decrypt(texto)
# print(test)



def esconde(msg):
    s = ''
    for c in msg: s += chr(ord(c) + 30000)
    return s
   
def mostra(msg):
    s = ''
    for c in msg: s += chr(ord(c) - 30000)
    return s

p = input('Digite a senha -> ')

print(esconde(p))
print(mostra(p))
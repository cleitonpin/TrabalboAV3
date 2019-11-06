import hashlib

senha = input('digite a senha: ')
hash = hashlib.md5(str(senha).encode(''))

senhaMD5 = hash.hexdigest()


print(senhaMD5)
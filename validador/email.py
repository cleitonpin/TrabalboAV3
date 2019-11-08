def valida(email):
    return email.find('@') == -1 or email.find('.com') == -1
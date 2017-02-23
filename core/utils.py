CCC = '@ccc.ufcg.edu.br'
DSC = '@dsc.ufcg.edu.br'
COMP = '@computacao.ufcg.edu.br'

def validate_email(email):
    n = len(email)
    if len(email) < 16:
        return False
    if email[n-16:n] == CCC or email[n-16:n] == DSC or email[n-23:n] == COMP:
        return True
    else:
        return False

def check_user(username, users):
    for u in users:
        if u.username == username:
            return False
    return True

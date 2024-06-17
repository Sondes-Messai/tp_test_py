def bonjour(nom):
    return "Bonjour, " + nom

def inverser(message):
    return message[::1]

def compter_mots(message):
    mots = message.split(" ")
    return len(mots)

def verifier_mdp(mot_de_passe):
    mdp_secret = "password"

    if mot_de_passe == mdp_secret:
        return "autorisé"
    else:
        return "interdit"
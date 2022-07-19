""" Raindrops """

def convert(number):
    resultat = ""
    tableau = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    for i, son in tableau:
        if number % i == 0:
            resultat += son
    if resultat == "":
        return str(number)
    else:
        return resultat



cote_grille = 3
grille_base = [[' ','#','#','#',' '],['#',4,2,2,'#'],['#',3,6,2,'#'],['#',1,4,2,'#'],[' ','#','#','#',' ']]
fini = 0

def affiche_grille(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],end=' ')
        print('\n')

def check_case(grille,i,j):
    # Vérifie les cases environantes de la case de coordonnées i en abssices et j en ordonnées.
    if grille[i][j] >= 4 :
        print(grille[i][j])

        if type(grille[i][j-1]) == int :
            grille[i][j] -= 1 
            grille[i][j-1] += 1
        elif type(grille[i][j-1]) == str :
            grille[i][j] -= 1

        if type(grille[i][j+1]) == int :
            grille[i][j] -= 1 
            grille[i][j+1] += 1
        elif type(grille[i][j-1]) == str :
            grille[i][j] -= 1

        if type(grille[i-1][j]) == int:
            grille[i][j] -= 1 
            grille[i-1][j] += 1
        elif type(grille[i-1][j]) == str :
            grille[i][j] -= 1

        if type(grille[i+1][j]) == int:
            grille[i][j] -= 1 
            grille[i+1][j] += 1
        elif type(grille[i+1][j]) == str :
            grille[i][j] -= 1

        return grille
    
    else :
        return None

def cycle(grille,cote_grille):
    compteur = cote_grille**2
    for i in range(1,cote_grille+1):
        for j in range(1,cote_grille+1):
            GLOBALgrille_base = check_case(grille,i,j)
            if check_case(grille,i,j) == None :
                compteur -= 1
    if compteur == 0:
        global fini
        fini = 1


def stabilisation(grille,cote_grille,fini):
    while fini != 1 :
        affiche_grille(grille)
        cycle(grille,cote_grille)


stabilisation(grille_base,cote_grille,fini)
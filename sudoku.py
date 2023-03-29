##### MOHELLIBI YANIS ###### 22003018 TD01 LSIN304

grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1=[
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]
grille_3 = [     
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 0, 5, 9, 0, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 0, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

def afficher(x):
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1,9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])

"""2.1 Fonctions de base"""

def unique(x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j] and x[j] != 0:
                return False
    return True

liste_teste_vrais = [0, 1, 0, 0, 2, 8, 9, 6, 4]
liste_teste_faux = [9, 0, 1, 0, 0, 2, 8, 9, 6, 4]

#print(unique(liste_teste_faux))
#print(unique(liste_teste_vrais))

def ligne(x, i):
    ligne_i = x[i-1]
    return ligne_i

#print(ligne(grille_2, 1))

def colonne(x, i):
    colonne_i = [ligne[i-1] for ligne in x]
    return colonne_i

#print(colonne(grille_2, 1))

"""  Les variables debut_colonne et debut_ligne on été trouver à partir de k = 3 * ((i - 1)//3) + ((j - 1)//3) + 1 pour ne pas
devoir baleyer toutes les cases du sudoku à chaques fois.   """

def region(x, i):
    debut_ligne = ((i-1) // 3) * 3
    debut_colonne = ((i-1)*3) % 9
    region_i = [x[ligne][colonne] for ligne in range(debut_ligne, debut_ligne + 3) for colonne in range(debut_colonne, debut_colonne + 3) ]
    return region_i

print(region(grille_2, 1))

def ajouter(x, i, j, v):
    k = 3 * ((i-1) //3 ) + ((j-1) // 3) + 1
    if 0 < v < 10 and 0 < i < 10 and 0 < j < 10 and x[i-1][j-1] == 0 :
        x[i-1][j-1] = v
        verif_ligne = unique(ligne(x, i))
        verif_colonne = unique(colonne(x, j))
        verif_region = unique(region(x, k))
        if verif_ligne == verif_colonne == verif_region == True:
            return x
        else:
            x[i-1][j-1] = 0
            return x
    else:
        print("vous ne respecté pas les règles, veuillez réessayer")
    
    
#afficher(ajouter(grille_0, 5, 5, 2))

def verifier(x):
    verif_grille = True
    for i in range(1,10):
        for j in range(1,10):
            k = 3 * ((i-1) //3 ) + ((j-1) // 3) + 1
            verif_colonne = unique(colonne(x, j))
            verif_region = unique(region(x, k))
            verif_ligne = unique(ligne(x, i))
            if (verif_ligne == False) or (verif_colonne == False) or (verif_region == False) or (x[i-1][j-1] == 0):
                verif_grille = False
    return verif_grille

#print(verifier(grille_2))

def jouer(x):
    afficher(x)
    while verifier(x) == False:
        i, j, v = int(input("Entrer le numéro de la ligne(i):")), int(input("Entrer le numéro de la colonne(j):")), int(input("Entrer la valeur(v):"))
        ajouter(x, i, j, v)
        afficher(x)
    else:
        return print("Bravo!, vous avez fini le Sudoku")

#jouer(grille_3)


"""2.2 Génération et résolution de grilles"""

def solution(x):
    dico_valeur = {}
    for clef in range(10):
        dico_valeur[clef] = []
    for i in range(1,10):
        for j in range(1,10):
            if x[i-1][j-1] == 0:
                l = []
                for v in range(1,10):
                    k = 3 * ((i-1) //3 ) + ((j-1) // 3) + 1
                    x[i-1][j-1] = v
                    verif_ligne = unique(ligne(x, i))
                    verif_colonne = unique(colonne(x, j))
                    verif_region = unique(region(x, k))
                    if verif_ligne == verif_colonne == verif_region == True:
                        l.append(v)
                    x[i-1][j-1] = 0
                dico_valeur[len(l)] += (i, j, l),
    return dico_valeur

#print(solution(grille_1))

def resoudre(x):
    dico_valeur = solution(x)
    l = [valeur for valeur in dico_valeur.values() if valeur != []]
    if dico_valeur[0] != []:
        return False
    if l == []:
        return afficher(x)
    for sous_liste in l:
        for tuple in sous_liste:
            i = tuple[0]
            j = tuple[1]
            v = tuple[2]
            for t in v:
                x[i -1][j -1] = t
                if resoudre(x) == False:
                    x[i -1][j -1] = 0
                else:
                    resoudre(x)            
            if resoudre != x:
                return False

#resoudre(grille_1)

from random import shuffle, randint

""" RecursionError de temps en temps. donc j'utilise la fonction setrecursionlimit() importer de sys """

from sys import setrecursionlimit
setrecursionlimit(10000)

def generer(x):
    dico_valeur = solution(x)
    l = [valeur for valeur in dico_valeur.values() if valeur != [] ]
    if l == []:
        return x
    if dico_valeur[0] == []:
        i = l[0][0][0]
        j = l[0][0][1]
        shuffle(l[0][0][2])
        t = l[0][0][2][0]
        x[i -1][j -1] = t

    elif dico_valeur[0] != []:
        x = grille_0
    return generer(x)

#afficher(generer(grille_0))


    
"""c'est possible que ce soit long 1 fois sur 2 """ 

def nouvelle():
    x = generer(grille_0)
    for case in range(64):
        i = randint(0, 8)
        j = randint(0, 8)
        x[i][j] = 0
    return afficher(x)

#nouvelle()



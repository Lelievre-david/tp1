#fonction pour lire les jeux de tests
import os

#fonction pour lire les jeux de tests
def read_file():
    #les jeux de tests sont dans le dossier TestsTP1
    files = os.listdir("TestsTP1")
    tests = []

    #pour chaque fichier
    for filename in files:
        #ouvrir le fichier
        file = open("TestsTP1/" + filename, "r")
        #lire le fichier
        lines = file.readlines()
        #la 1ere ligne contient les dimensions de la surface
        dimensions = lines[0].split()
        l, h = int(dimensions[0]), int(dimensions[1])
        #on recupere le nombre de points
        n = int(lines[1])
        #on recupere les points
        points = []
        for i in range(2, n+2):
            point = lines[i].split()
            points.append([int(point[0]), int(point[1])])
        
        #on ajoute le jeu de test a la liste des tests
        tests.append([l, h, n, points])
    #on retourne les donnees
    return tests

#algo 1 avec complexite O(n^3)
def find_max_rectangle(l, h, n, t):
    max_area = 0

    #on ajoute les points initiaux et finaux du plan dans la liste des points
    t.insert(0, [0, 0])
    t.append([l, h])

    #on parcourt tous les points pour les comparer entre deux à deux
    for i in range(len(t) - 1):
        for j in range(i + 1, len(t)):

            #la largeur maximale possible pour un rectangle situé entre ces 2 points est la distance entre les deux points
            width_possible = abs(t[j][0] - t[i][0])
            # Initialise la hauteur maximale possible à la hauteur du plan
            height_possible = h

            #on parcourt tous les points pour savoir si un point est situé entre les deux points d'indice i et j
            for k in range(0, len(t)):
                #si le point est situé entre les deux points d'indice i et j
                if t[k][0] > t[i][0] and t[k][0] < t[j][0]:

                    #on met à jour la hauteur maximale possible avec la hauteur du point
                    height_possible = min(height_possible, t[k][1])  

            #on calcule l'aire maximale possible pour un rectangle situé entre les deux points d'indice i et j
            area_possible = width_possible * height_possible
            #si l'aire maximale possible est supérieure à l'aire maximale actuelle, on met à jour l'aire maximale
            max_area = max(max_area, area_possible)

    return max_area

#algo 2 avec complexite O(n^2)
def find_max_rectangle2(l, h, n, t):
    max_area = 0

    t.insert(0, [0, 0])
    t.append([l, h])

    for i in range(len(t) - 1):
        
        #cette fois-ci, on intialise la hauteur max possible à chaque itération de i car on ne parcourt plus tous les points pour trouver la hauteur max possible
        height_possible = h

        for j in range(i + 1, len(t)):
            width_possible = abs(t[j][0] - t[i][0])

            area_possible = width_possible * height_possible
            max_area = max(max_area, area_possible)

            #si la hauteur du point est inférieure à la hauteur max possible, on met à jour la hauteur max possible pour les prochains rectangles possibles
            if t[j][1] < height_possible:
                height_possible = t[j][1]

    return max_area

#tester la fonction
tests = read_file()
for test in tests:
    l, h, n, points = test
    if n <= 500: #on ne teste que les jeux de tests de moins de 500 points pour des question de performance
        print(find_max_rectangle2(l, h, n, points))

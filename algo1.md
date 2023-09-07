# TP1-Diviser pour régner - Le plus grand rectangle

Auteur : David Lelièvre
---
Date : 2023-09-07
---

## Objectifs
On cherche à trouver la surface maximum possible d'un rectangle contenu dans un plan de l par h, dont la base est situé sur l'axe des abcisses et dont l'intérieur ne contient aucun des n points situés sur le plan et dont on a les coordonnées.

## Première approche
Cette première approche est basé sur le fait que la base du rectangle doit être situé sur l'axe des abcisses. Ainsi, il aura forcément deux sommets de la forme (x<sub>i</sub>,0) et (x<sub>j</sub>,0). 
On peut donc exprimer la surface du rectangle comme étant : (x<sub>j</sub> - x<sub>i</sub>) * min(y<sub>i</sub>,y<sub>j</sub>)
On peut en déduire un algorithme de complexité O(n<sup>3</sup>), qui va parcourir les points deux à deux, et pour chaque couple de points, va parcourir une 3eme fois les points pour regarder si il n'y a pas de points situé entre les deux points courants.

Pseudo-code:

```
entrée:
l: entiers, largeur du plan
h: entiers, hauteur du plan
n: entiers, nombre de points
points: liste de n tuples, contenant les coordonnées des n points

sortie : 
surface_max: entier, surface maximum du rectangle

fonction trouver_surface_max(l,h,n,points)
    surface_max = 0

    pour i de 0 à n-1
        pour j de i+1 à n-1
            largeur_possible = points[j][0] - points[i][0]
            hauteur_possible = h

            pour k de 0 à n-1
                si points[k][0] > points[i][0] et points[k][0] < points[j][0]
                    si points[k][1] < hauteur_possible
                        hauteur_possible = points[k][1]
                    fin si
                fin si
            fin pour

            surface_possible = largeur_possible * hauteur_possible
            si surface > surface_max
                surface_max = surface_possible

            fin si
        fin pour
    fin pour
    retourner surface_max
```
Cet algorithme est bien de complexité O(n<sup>3</sup>) car nous avons 3 boucles qui itèrent de 0 à n avec un pas de 1. Cependant il n'est pas tout à fait fonctionnel car il ne prends pas en compte les parties situées avant le premier point et après le dernier point, ainsi dans le test ne contenant aucun point sur le plan, il va nous donner une surface de 0. Pour modifier cela, il suffit simplement de rajouter dans la liste deux points dont l'un a son abcisse à 0 et l'autre a l'abcisse à l, les ordonnées ne sont pas importantes. Il faut bien penser à retrier la liste par abcisse croissante après avoir rajouté ces deux points.

On a donc le pseudo-code suivant:

```
entrée:
l: entiers, largeur du plan
h: entiers, hauteur du plan
n: entiers, nombre de points
points: liste de n tuples, contenant les coordonnées des n points

sortie :
surface_max: entier, surface maximum du rectangle

fonction trouver_surface_max(l,h,n,points)
    surface_max = 0

    ajouter (0,0) à points
    ajouter (l,0) à points
    trier points par ordre croissant de l'abcisse
    pour i de 0 à n-1
        pour j de i+1 à n-1
            largeur_possible = points[j][0] - points[i][0]
            hauteur_possible = h

            pour k de 0 à n-1
                si points[k][0] > points[i][0] et points[k][0] < points[j][0]
                    si points[k][1] < hauteur_possible
                        hauteur_possible = points[k][1]
                    fin si
                fin si
            fin pour

            surface_possible = largeur_possible * hauteur_possible
            si surface > surface_max
                surface_max = surface_possible

            fin si
        fin pour
    fin pour
    retourner surface_max
```
En implémentant cet algorithme en python (voir fichier alog1.py), on se rends compte que cet algorithme n'est pas très efficace, en effet, lorsque l'on test avec un nombre de points de 100000, il faut attendre plus de 15min pour obtenir une réponse. Cela ne semble donc pas combatible avec les demandes de CodeChef qui souhaitent que l'algorithme s'exécute en moins de 1s sur leur site.

Pour réduire la complexité de O(n<sup>3</sup>) à O(n<sup>2</sup>), il faut trouver un moyen de ne pas parcourir les points à chaque fois pour trouver la hauteur possible. Pour cela, on peut fixer la hauteur_possible courante à chaque itération de la boucle i. Ensuite, on peut parcourir les points une seule fois pour trouver la largeur_possible, et si elle est plus grande que la largeur_max, on peut recalculer la surface à partir de la hauteur_possible courante et de la largeur_possible courante et si celle-ci est supérieur à surface_max, on peut la remplacer. Enfin, il faut penser à mettre à jour la hauteur_possible à la fin de la boucle j si le point j courant à une hauteur plus petite que la hauteur_possible précédente.

On a donc le pseudo-code suivant:

```
entrée:
l: entiers, largeur du plan
h: entiers, hauteur du plan
n: entiers, nombre de points
points: liste de n tuples, contenant les coordonnées des n points

sortie :
surface_max: entier, surface maximum du rectangle

fonction trouver_surface_max(l,h,n,points)
    surface_max = 0

    ajouter (0,0) à points
    ajouter (l,0) à points
    trier points par ordre croissant de l'abcisse
    pour i de 0 à n-1
        hauteur_possible = h
        pour j de i+1 à n-1
            largeur_possible = points[j][0] - points[i][0]

            surface_possible = largeur_possible * hauteur_possible
            si surface_possible > surface_max
                surface_max = surface_possible
            fin si

            si points[j][1] < hauteur_possible
                hauteur_possible = points[j][1]
            fin si
        fin pour
    fin pour

    retourner surface_max
```
Nous avons cette fois-ci de meilleur performance que l'algorithme précèdent mais cela ne réponds toujours pas aux attentes de CodeChef. En effet, pour un nombre de points de 100000, il faut attendre plus de 10min pour obtenir une réponse. Il faut donc trouver un moyen de réduire encore la complexité de l'algorithme.







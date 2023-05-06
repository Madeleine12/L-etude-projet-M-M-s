from os import listdir, mkdir
import cv2
import numpy as np

# nom du dossier contenant les images
dossier = "toutes_images"

nb_bleu = []
nb_jaune = []
nb_marron = []
nb_orange = []
nb_rouge = []
nb_vert = []

# liste des images du dossier
images = listdir(dossier)


def filtre(image, bande_basse, bande_haute):
    lower_bound = np.array(bande_basse)
    upper_bound = np.array(bande_haute)
    new = cv2.inRange(image, lower_bound, upper_bound)
    return new


def homogeneite(photo):
    kernel = np.ones((3, 3), np.uint8)
    new = cv2.erode(photo, kernel, iterations=3)
    new = cv2.dilate(new, kernel, iterations=17)
    new = cv2.erode(new, kernel, iterations=4)
    return new


def connect_component(photo):
    photo = cv2.threshold(photo, 127, 255, cv2.THRESH_BINARY)[1]
    num_labels, _ = cv2.connectedComponents(photo)
    return num_labels - 1


for nom_image in images:
    nom = dossier + "/" + nom_image
    im = cv2.imread(nom)

    convertie = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # FILTRES
    bleu = filtre(im, [120, 70, 0], [255, 95, 20])
    jaune = filtre(im, [0, 160, 190], [50, 210, 240])
    marron = filtre(convertie, [0, 90, 80], [10, 170, 100])
    orange = filtre(im, [35, 115, 220], [50, 140, 255])
    rouge = filtre(im, [50, 50, 140], [60, 70, 210])
    vert = filtre(im, [10, 90, 30], [90, 255, 80])

    # HOMOGENEITE
    bleu = homogeneite(bleu)
    jaune = homogeneite(jaune)
    marron = homogeneite(marron)
    orange = homogeneite(orange)
    rouge = homogeneite(rouge)
    vert = homogeneite(vert)

    # CONNECT COMPONENT
    nb_bleu += [connect_component(bleu)]
    nb_jaune += [connect_component(jaune)]
    nb_marron += [connect_component(marron)]
    nb_orange += [connect_component(orange)]
    nb_rouge += [connect_component(rouge)]
    nb_vert += [connect_component(vert)]


# CALCUL DE PROPORTIONS
tot_bleu = 0
tot_jaune = 0
tot_marron = 0
tot_orange = 0
tot_rouge = 0
tot_vert = 0
for nom_image in nb_bleu:
    tot_bleu += nom_image
for nom_image in nb_jaune:
    tot_jaune += nom_image
for nom_image in nb_marron:
    tot_marron += nom_image
for nom_image in nb_orange:
    tot_orange += nom_image
for nom_image in nb_rouge:
    tot_rouge += nom_image
for nom_image in nb_vert:
    tot_vert += nom_image

TOT = tot_bleu + tot_jaune + tot_marron + tot_orange + tot_rouge + tot_vert
p_bleu = tot_bleu / TOT
p_jaune = tot_jaune / TOT
p_marron = tot_marron / TOT
p_orange = tot_orange / TOT
p_rouge = tot_rouge / TOT
p_vert = tot_vert / TOT

print("proportion de bleus", p_bleu)
print("proportion de jaunes", p_jaune)
print("proportion de marrons", p_marron)
print("proportion de oranges", p_orange)
print("proportion de rouges", p_rouge)
print("proportion de verts", p_vert)

print("bleu", tot_bleu)
print("jaune", tot_jaune)
print("maron", tot_marron)
print("orange", tot_orange)
print("rouge", tot_rouge)
print("verts", tot_vert)

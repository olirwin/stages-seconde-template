# RUBIKA - SNAKE GAME

# Importation des bibliothèques, ne pas modifier
import pygame
import random


# Initialisation des couleurs, ne pas modifier
blanc = (255, 255, 255)
jaune = (255, 255, 102)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Etape 1: Définition des variables


# Etape 2.3: Dessiner un carré dans la fenêtre, remplacez '...' par les bonnes variables
def dessine_carre(x: int, y: int, couleur: tuple):
    pygame.draw.rect(surface=..., color=..., rect=...)


# Etape 4: Dessiner plusieurs carrés à partir d'une liste de position et d'une couleur


# Etape 3.1: Obtenir un nombre aléatoire entre 0 et max (exclus), remplacez les '...' par les bonnes valeurs ou variables
def entier_aleatoire(max):
    return random.randint(..., ...)


# Etape 3.2: Obtenir des coordinées aléatoire dans la fenêtre


# Affiche un message dans le coin supérieur gauche de la fenêtre en Comic Sans MS, taille 20
def afficher_message(message: str, couleur: tuple):
    fenetre.blit(pygame.font.SysFont("comicsansms", 20).render(message, True, couleur), [0, 0])


# Etape 7: Obtenir la nouvelle direction en fonction de la touche appuyée


# Etape 9: Obtenir la nouvelle position en fonction de la direction actuelle


# Etape 10: Vérifier si la postion est située dans la fenêtre


# Un tour de jeu
def tour_de_jeu(positions_serpent, fin_jeu, direction_serpent, position_pomme):
    # Etape 6.1: Afficher la pomme

    # Etape 6.2: Afficher le score

    # Etape 6.3: Afficher le serpent

    # Mise à jour de la fenêtre
    pygame.display.update()

    # Récupération des touches appuyées
    for event in pygame.event.get():
        # Etape 8.1: On a cliqué sur la croix, on ferme le jeu, remplacez '...' par le bon code
        ...

        # Etape 8.2: Une touche est appuyée, on met à jour la direction, remplacez '...' par le bon code
        ...

    # Etape 11: Etape 11: Quelle est la future position du serpent ? Est-ce dans la zone ?

    # Etape 12: Le serpent est-il sur une pomme ?

    return positions_serpent, fin_jeu, direction_serpent, position_pomme


# Initialisation de la fenêtre de jeu
pygame.init()  # ne pas modifier

# Etape 2.1: Remplacer (..., ...) par les bonnes variables
fenetre = pygame.display.set_mode((..., ...))

# Définition du nom de la fenêtre
pygame.display.set_caption("Snake")

# Etape 5: Définition des variables d'environnement du jeu, remplacer les '...' par les bonne valeurs
positions_serpent = ...
fin_jeu = ...
direction_serpent = ...
position_pomme = ...

# Définition de l'horloge interne du jeu, augmenter 'tick' pour augmenter la vitesse du jeu
clock = pygame.time.Clock()  # ne pas modifier
tick = 10

# Etape 6.4: Tant que le jeu n'est pas fini, remplacer '...' par la bonne variable
while ...:
    # Etape 2.2: On remplit le fond d'une couleur, remplacer '...' par la bonne variable
    fenetre.fill(...)

    # Mise à jour des variables du jeu
    positions_serpent, fin_jeu, direction_serpent, position_pomme = tour_de_jeu(positions_serpent, fin_jeu, direction_serpent, position_pomme)
    clock.tick(tick)  # ne pas modifier

# Fin du jeu
print("Game Over")
pygame.quit()
quit()

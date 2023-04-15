# Importation des bibliothèques nécessaires
import sys
import random
import pygame
from pygame.locals import QUIT
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import QUIT, DOUBLEBUF, OPENGL

# Définition de la taille de la fenêtre
WIDTH = 800
HEIGHT = 800

# Définition des transformations de Barnsley sous forme de tuples
TRANSFORMATIONS = [
    (0.01, 0.0, 0.0, 0.16, 0.0, 0.0, 0.01),
    (0.85, 0.04, -0.04, 0.85, 0.0, 1.6, 0.85),
    (0.2, -0.26, 0.23, 0.22, 0.0, 1.6, 0.07),
    (0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07)
]

# Fonction qui applique une transformation à un point (x, y) en fonction d'un tuple de transformation t
def apply_transformation(x, y, t):
    a, b, c, d, e, f, p = t
    return a * x + b * y + e, c * x + d * y + f

# Fonction qui sélectionne aléatoirement une des transformations en fonction de leurs probabilités
def random_transformation():
    r = random.random()
    for t in TRANSFORMATIONS:
        if r <= t[6]:
            return t
        r -= t[6]

# Fonction qui génère le fractal de Barnsley en appliquant des transformations aléatoires à un point de départ (0, 0)
def barnsley_fractal(iterations):
    x, y = 0, 0
    points = []
    for _ in range(iterations):
        x, y = apply_transformation(x, y, random_transformation())
        points.append((x, y))
    return points

# Fonction principale
def main():
    # Initialisation de la bibliothèque Pygame et de la fenêtre
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    # Configuration de la vue OpenGL en 2D
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    # Définition de la couleur de fond de l'écran
    glClearColor(0, 0, 0, 1)

    # Boucle principale du programme
    while True:
        # Écoute des événements Pygame, tels que la fermeture de la fenêtre
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Effacement de l'écran et début du dessin de points avec OpenGL
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)

        # Génération du fractal de Barnsley et dessin de chaque point
        points = barnsley_fractal(50000)
        glColor3f(0, 1, 0) # Couleur des points
        for x, y in points:
            # Conversion des coordonnées normalisées en coordonnées réelles et dessin du point
            glVertex2f((x + 2.5) * WIDTH // 6, (y + 0.5) * HEIGHT // 12)

        glEnd()
        pygame.display.flip()
        pygame.time.wait(1000)

if __name__ == "__main__":
    main()

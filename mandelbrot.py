import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

def mandelbrot(c):
    # Calcule le nombre d'itérations nécessaires pour déterminer si la coordonnée c appartient à l'ensemble de Mandelbrot
    z = 0
    for i in range(100):
        # Ajoute une petite perturbation aléatoire à la valeur de z à chaque itération pour ajouter un peu d'aléatoire
        # Notez que la valeur de la perturbation est fixée à (-0.1, 0.1) pour rester relativement petit
        z = z*z + c + complex(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
        if abs(z) > 2:
            # Si la valeur de z dépasse 2, la coordonnée c n'appartient pas à l'ensemble de Mandelbrot
            # et nous retournons le nombre d'itérations effectuées avant de sortir de la boucle
            return i
    # Si la boucle se termine sans que la valeur de z ne dépasse 2, la coordonnée c est probablement dans l'ensemble de Mandelbrot
    # et nous retournons 0 pour indiquer cela
    return 0

def draw_mandelbrot():
    # Dessine l'ensemble de Mandelbrot en bouclant à travers chaque pixel de l'écran
    glBegin(GL_POINTS)
    for x in range(-400, 400):
        for y in range(-300, 300):
            # Calcule la coordonnée complexe correspondant au pixel actuel
            c = complex(x/200.0, y/200.0)
            # Calcule le nombre d'itérations nécessaires pour déterminer si la coordonnée c appartient à l'ensemble de Mandelbrot
            i = mandelbrot(c)
            # Calcule la valeur de couleur pour ce pixel en fonction du nombre d'itérations effectuées
            # Notez que la valeur de r est limitée à 1 pour éviter les couleurs trop claires
            r = min(i/100.0, 1.0)
            # Définit la couleur du pixel en fonction de la valeur de r
            glColor3f(r, r, r)
            # Dessine le pixel à l'écran
            glVertex2f(x, y)
    glEnd()

# Initialise Pygame et OpenGL, définit la taille de l'écran et configure la projection et la vue OpenGL
pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF|OPENGL)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-400, 400, -300, 300)
glMatrixMode(GL_MODELVIEW)
clock = pygame.time.Clock()

# Boucle principale qui dessine l'ensemble de Mandelbrot et gère les événements
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)
    draw_mandelbrot()
    pygame.display.flip()
    clock.tick(30)

# Ferme Pygame proprement et quitte Python
pygame.quit()
quit()

import sys
import random
import pygame
from pygame.locals import QUIT, DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D

# Paramètres de la fenêtre
WIDTH = 800
HEIGHT = 800

def random_transformations(num_transformations):
    transformations = []
    for _ in range(num_transformations):
        a, b, c, d = [random.uniform(-1, 1) for _ in range(4)]
        e, f = [random.uniform(0, 1) for _ in range(2)]
        p = random.uniform(0, 1)
        transformations.append((a, b, c, d, e, f, p))
    total_p = sum(t[6] for t in transformations)
    return [(a, b, c, d, e, f, p / total_p) for a, b, c, d, e, f, p in transformations]

TRANSFORMATIONS = random_transformations(4)

def apply_transformation(x, y, t):
    a, b, c, d, e, f, p = t
    return a * x + b * y + e, c * x + d * y + f

def random_transformation():
    r = random.random()
    for t in TRANSFORMATIONS:
        if r <= t[6]:
            return t
        r -= t[6]

def barnsley_fractal(iterations):
    x, y = 0, 0
    points = []
    for _ in range(iterations):
        x, y = apply_transformation(x, y, random_transformation())
        points.append((x, y))
    return points

def random_color():
    return random.random(), random.random(), random.random()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glClearColor(0, 0, 0, 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)

        points = barnsley_fractal(50000)
        for x, y in points:
            glColor3f(*random_color())
            glVertex2f((x + 2.5) * WIDTH // 4, (y + 0.5) * HEIGHT // 4)

        glEnd()
        pygame.display.flip()
        pygame.time.wait(1000)

        # Générer de nouvelles transformations pour la prochaine itération
        TRANSFORMATIONS = random_transformations(4)

if __name__ == "__main__":
    main()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def create_patatoid(radius, detail):
    vertices = []
    for i in range(detail + 1):
        lat = i * np.pi / detail - np.pi / 2
        for j in range(detail * 2):
            lon = j * np.pi / detail
            x = radius * np.cos(lat) * np.cos(lon)
            y = radius * np.cos(lat) * np.sin(lon)
            z = radius * np.sin(lat)

            perturbation = np.random.uniform(0.9, 1.1)
            vertices.append((x * perturbation, y * perturbation, z * perturbation))

    faces = []
    for i in range(detail):
        for j in range(detail * 2):
            idx1 = i * detail * 2 + j
            idx2 = i * detail * 2 + (j + 1) % (detail * 2)
            idx3 = (i + 1) * detail * 2 + j
            idx4 = (i + 1) * detail * 2 + (j + 1) % (detail * 2)

            faces.append((idx1, idx2, idx4, idx3))
    return vertices, faces

def face_color(vertex):
    _, y, z = vertex
    r = 0.5 * (y + 1)
    g = 0.5 * (z + 1)
    b = 1 - r - g
    return (r, g, b)

def draw_patatoid(vertices, faces):
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glColor3fv(face_color(vertices[vertex]))
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    vertices, faces = create_patatoid(radius=1, detail=20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_patatoid(vertices, faces)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

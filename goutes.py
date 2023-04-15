import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random

class Particle:
    def __init__(self, position, velocity, size):
        self.position = np.array(position, dtype=np.float32)
        self.velocity = np.array(velocity, dtype=np.float32)
        self.size = size

    def update(self, dt):
        self.position += self.velocity * dt

def draw_particle(particle):
    glPushMatrix()
    glTranslatef(*particle.position)
    glBegin(GL_QUADS)
    glVertex3f(-particle.size, -particle.size, 0)
    glVertex3f(particle.size, -particle.size, 0)
    glVertex3f(particle.size, particle.size, 0)
    glVertex3f(-particle.size, particle.size, 0)
    glEnd()
    glPopMatrix()

def simulate_and_draw(particles, dt):
    for particle in particles:
        particle.update(dt)
        draw_particle(particle)

def init_window_and_gl():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def create_new_particles():
    num_particles = 5
    x_spacing = 2.0 / num_particles
    particles = []

    for i in range(num_particles):
        x_position = -1 + i * x_spacing
        position = [x_position, 1, 0]
        velocity = [0, -0.1, 0]
        size = 0.05
        particles.append(Particle(position, velocity, size))

    return particles

def main_loop():
    clock = pygame.time.Clock()
    dt = 1 / 60
    running = True
    particles = create_new_particles()
    spawn_timer = 0
    spawn_interval = 4  # Temps en secondes

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        simulate_and_draw(particles, dt)
        pygame.display.flip()
        clock.tick(60)

        # Gérer le réapparition des particules
        spawn_timer += dt
        if spawn_timer >= spawn_interval:
            spawn_timer -= spawn_interval
            particles.extend(create_new_particles())

    pygame.quit()

if __name__ == "__main__":
    init_window_and_gl()
    main_loop()

import math
import random

NUM_PEOPLE = 100
MAX_SPEED = 5.0
GOAL_X = 100.0
GOAL_Y = 100.0
TIME_STEP = 0.1
WALL_X_MIN = 0.0
WALL_X_MAX = 200.0
WALL_Y_MIN = 0.0
WALL_Y_MAX = 200.0
WALL_FORCE_FACTOR = 0.1

class Person:
    def __init__(self, x, y, vx=0.0, vy=0.0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)

def update_person(person, people):
    # Calculate distance and force to goal
    dist_goal = distance(person.x, person.y, GOAL_X, GOAL_Y)
    force_goal_x = (GOAL_X - person.x) / dist_goal
    force_goal_y = (GOAL_Y - person.y) / dist_goal
    
    # Calculate distance and force to walls
    force_wall_x = 0.0
    force_wall_y = 0.0
    if person.x < WALL_X_MIN:
        force_wall_x += (WALL_X_MIN - person.x) * WALL_FORCE_FACTOR
    elif person.x > WALL_X_MAX:
        force_wall_x += (WALL_X_MAX - person.x) * WALL_FORCE_FACTOR
    if person.y < WALL_Y_MIN:
        force_wall_y += (WALL_Y_MIN - person.y) * WALL_FORCE_FACTOR
    elif person.y > WALL_Y_MAX:
        force_wall_y += (WALL_Y_MAX - person.y) * WALL_FORCE_FACTOR
    
    # Sum up forces
    force_total_x = force_goal_x + force_wall_x
    force_total_y = force_goal_y + force_wall_y
    
    # Update velocity and position
    speed = math.sqrt(person.vx * person.vx + person.vy * person.vy)
    if speed > MAX_SPEED:
        person.vx *= MAX_SPEED / speed
        person.vy *= MAX_SPEED / speed
    person.vx += force_total_x * TIME_STEP
    person.vy += force_total_y * TIME_STEP
    person.x += person.vx * TIME_STEP
    person.y += person.vy * TIME_STEP

people = [Person(random.uniform(0, WALL_X_MAX), random.uniform(0, WALL_Y_MAX)) for _ in range(NUM_PEOPLE)]

while distance(people[0].x, people[0].y, GOAL_X, GOAL_Y) > 1.0:
    for person in people:
        update_person(person, people)
        
    # Draw the simulation (using print as a placeholder)
    print("Time: %.1f" % TIME_STEP)
    for i, person in enumerate(people):
        print("Person %d: x=%.1f, y=%.1f" % (i, person.x, person.y))
        
print("Simulation finished.")

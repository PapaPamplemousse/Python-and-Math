import math
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

def update(frame_number, people, scat):
    for i in range(NUM_PEOPLE):
        update_person(people[i], people)

    x = [person.x for person in people]
    y = [person.y for person in people]

    scat.set_offsets(list(zip(x, y)))

    return scat

# Create initial positions for people
people = [Person(random.uniform(0, WALL_X_MAX), random.uniform(0, WALL_Y_MAX)) for _ in range(NUM_PEOPLE)]

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(WALL_X_MIN, WALL_X_MAX)
ax.set_ylim(WALL_Y_MIN, WALL_Y_MAX)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Simulation')

# Create scatter plot of people
scat = ax.scatter([person.x for person in people], [person.y for person in people])

# Create animation
anim = animation.FuncAnimation(fig, update, fargs=(people, scat), interval=50)

# Show the plot
plt.show()


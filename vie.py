import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# Définition des dimensions de la grille
N = 100
M = 100

# Initialisation de la grille avec une configuration aléatoire
grid = np.random.randint(2, size=(N, M))

# Définition de la fonction de mise à jour de la grille à chaque étape
def update(frameNum, img, grid, N, M):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(M):
            # Calcul du nombre de voisins vivants pour chaque cellule
            neighbours = grid[(i-1)%N,(j-1)%M] + grid[(i-1)%N,j] + grid[(i-1)%N,(j+1)%M] + \
                        grid[i,(j-1)%M] + grid[i,(j+1)%M] + \
                        grid[(i+1)%N,(j-1)%M] + grid[(i+1)%N,j] + grid[(i+1)%N,(j+1)%M]
            # Règles du Jeu de la Vie
            if grid[i, j] == 1 and (neighbours < 2 or neighbours > 3):
                newGrid[i, j] = 0
            elif grid[i, j] == 0 and neighbours == 3:
                newGrid[i, j] = 1
    # Mise à jour de la grille
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Initialisation de l'animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, M), frames=100, interval=50, 
                              save_count=50)

plt.show()

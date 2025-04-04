from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
plt.close("all")

with open('labyrinth.txt') as fin:
    grid = [list(map(int,l.strip())) for l in fin]

cmap = ListedColormap(['#ffffff','#000000','#145298'])
fig, ax = plt.subplots(1, 1, figsize=(12, 5))
ax.imshow(grid, cmap=cmap, interpolation='nearest')
plt.tight_layout()
plt.show()

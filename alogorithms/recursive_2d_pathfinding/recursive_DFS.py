from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from copy import deepcopy

with open('labyrinth.txt') as fin:
    grid = [list(map(int,l.strip())) for l in fin]
    edit_grid = deepcopy(grid)
    grid_w = len(grid[0])
    grid_h = len(grid)

plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(edit_grid, cmap=ListedColormap(['#ffffff','#000000','#145298','#ff5298','yellow']), interpolation='nearest', vmin=0, vmax=4)
plt.show()

directions = ((0,1),(1,0),(0,-1),(-1,0))

def a_star(pos:tuple[int,int], visited:set[tuple[int,int]]=set(), out:list[tuple[int,int]]=[]):
    
    x,y = pos

    # matplotlib
    edit_grid[y][x] = 2
    img.set_data(edit_grid)
    plt.pause(.05)

    for dx,dy in directions:
        npos = nx,ny = x+dx, y+dy
        if npos in visited:
            continue
        if not (0 <= nx < grid_w) or not (0 <= ny < grid_h):
            continue
        if grid[ny][nx] == 1:
            continue
        elif grid[ny][nx] == 3:
            print("FINE!")
            out.append(pos)
            return True
        visited.add(npos)
        
        if a_star(npos, visited, out):
            out.append(pos)
            return True
        
if __name__ == '__main__':
    start = (0,1)
    path = []
    a_star(start,out=path)
    print(path)
    for x,y in path:
        edit_grid[y][x] = 4
        img.set_data(edit_grid)
        plt.pause(.05)
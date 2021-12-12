"""
A non optimal (87% validation) solution for Codingame's labyrinth puzzle.
Using Breadth-First Search graph exploration.
"""

import sys
import math

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]
STEP = False

# Rick's next move (UP DOWN LEFT or RIGHT).
def get_dir_str(dir, kr, kc):
    y,x = dir
    if y < kr:
        return "UP"
    elif y > kr:
        return "DOWN"
    elif x < kc:
        return "LEFT"
    else:
        return "RIGHT"

def get_childs(node, grid):
    y,x = node
    l = [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]                                  # All 4 potential neighbors
    l = [(y,x) for (y,x) in l if (y > 0 and y < r and x > 0 and x < c)]    # Filtering out out-of-grid coordinates
    return [(y,x) for (y,x) in l if (grid[y][x] != '#')]                   # Filtering out obstacles

def get_step(parents, start, node):
    y,x = node
    while(parents[y][x] != start):
        y,x = parents[y][x]
    return (y,x)

# BFS algorithm
def search(grid, start):
    global STEP
    sr,sc = start
    queue = []
    visited = []
    distance = []
    parents = []
    queue.append(start)

    for y in range(len(grid)):
        distance.append([])
        parents.append([])
        for x in range(len(grid[y])):
            distance[y].append(float('inf'))
            parents[y].append((-1,-1))
    distance[sr][sc] = 0
    visited.append(start)

    while(len(queue) > 0):
        s = queue.pop(0)
        childs = get_childs(s,grid)
        if( STEP ):
            childs = [(y,x) for (y,x) in childs if (grid[y][x] != 'C')]
        for i in childs:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                y,x = i
                parents[y][x] = (s)
                if(not STEP):
                    if(grid[y][x] == '?' or grid[y][x] == 'C'):
                        return get_step(parents,start,i)
                elif(STEP and grid[y][x] == 'T'):
                    return get_step(parents,start,i)
    return (-1,-1)
    
def get_dir(grid,start):
    global STEP
    dir = search(grid,start)
    if(dir == (-1,-1)):
        return search(grid,start)
    return dir

# game loop
while True:
    kr, kc = [int(i) for i in input().split()]
    grid = []
    for i in range(r):
        grid.append(input())

    if grid[kr][kc] == 'C':
        STEP = True

    dir = get_dir(grid,(kr,kc))
    dir_str = get_dir_str(dir,kr,kc)
    print(dir_str)
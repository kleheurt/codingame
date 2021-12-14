"""
A non optimal (87% validation) solution for Codingame's labyrinth puzzle.
Using Breadth-First Search graph exploration.
WIP
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
    if(parents[y][x] != start):
        return get_step(parents, start, parents[y][x])
    else :
        return (y,x)

# BFS algorithm
def search(grid, start):
    global STEP
    sr,sc = start
    queue = [start]
    visited = [start]
    distance = [[float('inf') for i in range(len(grid[j]))] for j in range(len(grid))]
    parents = [[(-1,-1) for i in range(len(grid[j]))] for j in range(len(grid))]
    distance[sr][sc] = 0
    return search_loop(queue, grid, visited, distance, parents, start)

def search_loop(queue, grid, visited, distance, parents, start):
    if(queue == []):
        return (-1,-1)
    else :
        s = queue.pop(0)
        childs = get_childs(s,grid)
        if( STEP ):
            childs = [(y,x) for (y,x) in childs if (grid[y][x] != 'C')] #leave CTRL room
        childs = [x for x in childs if x not in visited]
        for i in childs:
            queue.append(i)
            visited.append(i)
            y,x = i
            parents[y][x] = (s)
            if(not STEP):
                if(grid[y][x] == '?' or grid[y][x] == 'C'):
                    return get_step(parents,start,i)
            elif(STEP and grid[y][x] == 'T'):
                return get_step(parents,start,i)
    return search_loop(queue, grid, visited, distance, parents, start)
    
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

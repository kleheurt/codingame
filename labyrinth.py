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

def go_to(parents, currentNode, node):
    y,x = node
    if(parents[y][x] != currentNode):
        return go_to(parents, currentNode, parents[y][x])
    else :
        return (y,x)

# BFS algorithm
def search(grid, currentNode):
    sr,sc = currentNode
    queue = [currentNode]
    visited = [currentNode]
    parents = [[(-1,-1) for i in range(len(grid[j]))] for j in range(len(grid))]
    return search_loop(queue, grid, visited, parents, currentNode)

def search_loop(queue, grid, visited, parents, currentNode):
    if(queue == []):
        return (-1,-1)
    else :
        s = queue.pop(0)
        childs = get_childs(s,grid)
        childs = [x for x in childs if x not in visited]
        for (y,x) in childs:
            queue.append((y,x))
            visited.append((y,x))
            parents[y][x] = (s)
            if(not STEP):
                if(grid[y][x] == 'C' or grid[y][x] == '?'):
                    return go_to(parents,currentNode,(y,x))
            elif(STEP and grid[y][x] == 'T'):
                return go_to(parents,currentNode,(y,x))
    return search_loop(queue, grid, visited, parents, currentNode)
    
def get_dir(grid,currentNode):
    dir = search(grid,currentNode)
    if(dir == (-1,-1)):
        return search(grid,currentNode)
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

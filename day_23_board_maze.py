"""You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. 
Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board."""
def edges(node, n, m):
    node_i, node_j = node
    neighbours = [
        (node_i - 1, node_j),
        (node_i + 1, node_j),
        (node_i, node_j + 1),
        (node_i, node_j - 1),
    ]
    valid_neighbours = []
    for neighbour in neighbours:
        y, x = neighbour
        if 0 <= y < n and 0 <= x < m:
            valid_neighbours.append(neighbour)
    return valid_neighbours


def dfs_sol(board, start, end):
    table = dict()
    n = len(board)
    m = len(board[0])
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if (i, j) == end and board[i][j] == True:
                return "Not possible"
            table[(i,j)] = board[i][j]

    num_steps = 0
    pile = []
    visited = []
    pile.append(start)
    visited.append(start)
    while len(pile)>0:
        curr_node = pile[-1]
        #print(curr_node, "oooo")
        all_visited = True
        possible_neighbours = edges(curr_node, n, m)
        neighbours = [node for node in possible_neighbours if table[node] == False]
        #print(neighbours)
        for i in sorted(neighbours):
            if i not in visited:
                visited.append(i)
                all_visited = False
                next_node = i
                num_steps +=1
                if i == end:
                    return num_steps
                break
        if all_visited == False:
            pile.append(next_node)
            visited.append(next_node)
            #print(pile, "fsbfbu")
        else:
            pile.pop(-1)
            num_steps -=1
    return "Not possible"

print(dfs_sol([[True, True, True, False],
               [False, False, False, False],
               [True, False, True, True],
               [False, True, True, False]],
                 (1,0),(0,3)))

#NOTE: DFS!!!

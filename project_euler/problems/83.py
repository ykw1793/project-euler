import os
from . import usage

def solution():
    # PyPy ~ 800 ms

    def create_graph(mat):
        g = {(-1,-1): {(0,0): mat[0][0]}}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if (row, col) not in g:
                    g[(row, col)] = {}
                if row-1 >= 0: # up
                    g[(row, col)][(row-1, col)] = mat[row-1][col]
                if col-1 >= 0: # left
                    g[(row, col)][(row, col-1)] = mat[row][col-1]
                if row+1 < len(mat): # down
                    g[(row, col)][(row+1, col)] = mat[row+1][col]
                if col+1 < len(mat[0]): # right
                    g[(row, col)][(row, col+1)] = mat[row][col+1]
        return g

    with open(os.path.join(os.path.dirname(__file__), 'matrix_83.txt'), 'r') as f:
        mat = []
        for line in f.readlines():
            mat.append([int(x) for x in line.strip().split(',')])
        g = create_graph(mat)
        
        dist = {}
        init_node = (-1,-1)
        unvisited_nodes = []

        for node in g:
            dist[node] = 10**100
            unvisited_nodes.append(node)
        
        dist[init_node] = 0

        while len(unvisited_nodes) > 0:
            min_node = unvisited_nodes[0]
            min_dist = dist[min_node]

            for node in unvisited_nodes[1:]:
                if dist[node] < min_dist:
                    min_dist = dist[node]
                    min_node = node
            
            curr_node = min_node
            unvisited_nodes.remove(curr_node)

            for node in g[curr_node]:
                updated_min_dist = g[curr_node][node] + dist[curr_node]
                if updated_min_dist < dist[node]:
                    dist[node] = updated_min_dist
        
        return dist[(len(mat)-1, len(mat[0])-1)]

if __name__ == '__main__':
    usage.usage(solution, n=1)
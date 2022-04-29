
from turtle import color


def is_bipartite(adj):
    """
    Args:
        adj: adjacency list represents a graph
    
    Returns:
        True if the graph is bipartite else False
    """
    
    n = len(adj)
    # colors[i] is the color of node i, if colors[i] = -1 if node i is not colored
    colors = [-1] * n 
    
    def dfs(node):
        for neigh in adj[node]:
            if colors[neigh] != -1 and colors[neigh] == colors[node]:
                return False
            elif colors[neigh] == -1:
                colors[neigh] = 1 - colors[node]
                if not dfs(neigh):
                    return False
                    
        return True

    for i in range(n):
        if colors[i] == -1:
            colors[i] = 0
            if not dfs(i):
                return False
    
    return True


            
graph = [[1,3],[0,2],[1,3],[0,2]]

print(is_bipartite(graph))               
                

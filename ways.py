from functools import lru_cache


def ways(adj, src, des):
    """
    Args:
        adj: adjacency list represents a directed acyclic graph
        src: the source
        des: the destination

    Returns:
        the number of paths from src to des
    """
    
    @lru_cache(None)
    def dfs(cur):
        if cur == des:
            return 1
        
        return sum(dfs(neigh) for neigh in adj[cur])
    
    return dfs(src)


adj = [[] for i in range(10)]
adj[0] = [1, 2, 3]
adj[1] = [4]
adj[2] = [3, 5]
adj[3] = [4]
adj[4] = [6, 7]
adj[5] = [6, 8]
adj[6] = [7, 8, 9]
adj[7] = [9]
adj[8] = [9]
adj[9] = []

print([ways(adj, i, 9) for i in range(0, 9)])
    

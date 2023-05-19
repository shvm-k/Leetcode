class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)  # Number of nodes in the graph
        
        # Create a list to store the color of each node (-1: not colored, 0: color A, 1: color B)
        colors = [-1] * n
        
        # Perform depth-first search (DFS) starting from each uncolored node
        for node in range(n):
            if colors[node] == -1:
                if not self.dfs(node, 0, colors, graph):
                    return False
        
        return True
    
    def dfs(self, node, color, colors, graph):
        colors[node] = color  # Color the current node
        
        # Explore the neighbors of the current node
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False  # Conflict: neighbor has the same color
            if colors[neighbor] == -1 and not self.dfs(neighbor, 1 - color, colors, graph):
                return False  # Conflict found in the subgraph
            
        return True

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dest_nodes = set()
        for edge in edges:
            dest_nodes.add(edge[1])
        result = []
        
        for i in range(n):
            if i not in dest_nodes:
                result.append(i)
        return result

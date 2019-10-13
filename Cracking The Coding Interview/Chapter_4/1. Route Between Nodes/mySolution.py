"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        # write your code here
        visited = set()
        return self.dfs(graph, s, t, s, visited)
        
    def dfs(self, graph, s, t, cur, visited):
        if cur in visited:
            return False
        if cur == t:
            return True
        visited.add(cur)
        for neighbor in cur.neighbors:
            if self.dfs(graph, s, t, neighbor, visited):
                return True
        return False
        
            
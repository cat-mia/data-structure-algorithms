# leetcode305

# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]

class Solution:
    def __init__(self):
        self.father = {}
    
    def init(self, n):
        for i in range(n):
            self.father[i] = i
    
    def find(self,node):
        path = []
        cur = node
        while cur != self.father[cur]:
            path.append(cur)
            cur = self.father[cur]
        for n in path:
            self.father[n] = cur
        return cur

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        self.father[i] = j

    def numIslands(self, m, n, positions) -> int:
        # 实时更新一个全0的m*n grid
        pass
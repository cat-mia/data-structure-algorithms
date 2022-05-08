# https://leetcode-cn.com/problems/number-of-provinces/
# 并查集，dfs都可解

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

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.init(n)
        # 只遍历半个区域
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    self.union(i, j)
        s = set()
        for i in range(n):
            s.add(self.find(i))
        return len(s)
        
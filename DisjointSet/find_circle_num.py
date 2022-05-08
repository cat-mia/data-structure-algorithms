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
        
# or 复用代码
class Node:
    def __init__(self, val) -> None:
        self.val = val

class DisjointSet:
    def __init__(self, data_list) -> None:
        self.size_map = {} # 只存每个集合头节点
        self.father = {}
        self.nodes = {}
        self.add(data_list)

    def add(self, data_list):
        for v in data_list:
            node = Node(v)
            self.nodes[v] = node
            self.father[node] = node
            self.size_map[node] = 1

    def ancestor(self, node):
        path = []
        cur = node
        while cur != self.father[cur]:
            path.append(cur)
            cur = self.father[cur]
        for n in path:
            self.father[n] = cur
        return cur

    # 小的集合挂到大的集合上
    def union(self, x, y):
        x_a = self.ancestor(self.nodes[x])
        y_a = self.ancestor(self.nodes[y])
        if x_a == y_a:
            return
        small = x_a if self.size_map[x_a] > self.size_map[y_a] else y_a
        big = y_a if self.size_map[x_a] > self.size_map[y_a] else x_a
        self.father[small] = big
        self.size_map[big] = self.size_map[small] + self.size_map[big]
        del self.size_map[small]

class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        s = DisjointSet([_ for _ in range(n)])
        # 只遍历半个区域
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    s.union(i, j)
        return len(s.size_map)
        
s = Solution()
print(s.findCircleNum([[1,1,1],[1,1,1],[1,1,1]]))